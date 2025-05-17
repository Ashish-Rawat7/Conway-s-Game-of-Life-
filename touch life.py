import pygame
import random
import argparse
import os

def save_pattern(board, filename="pattern.txt"):
    """Save the current board state to a file."""
    with open(filename, "w") as file:
        for row in board:
            file.write("".join(map(str, row)) + "\n")

def load_pattern(filename="pattern.txt"):
    """Load a board state from a file."""
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return [[0] * len(board[0]) for _ in range(len(board))]  # Return an empty board if file not found

    with open(filename, "r") as file:
        return [list(map(int, line.strip())) for line in file]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int, default=60)
    parser.add_argument('--height', type=int, default=30)
    parser.add_argument('--fps', type=int, default=10)
    return parser.parse_args()

args = parse_args()


width, height = args.width, args.height
board = [[0]*width for _ in range(height)]

def count_neighbors(board, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0),  (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
            count += board[ny][nx]
    return count

def next_gen(board):
    height = len(board)
    width = len(board[0])
    new_board = [[0]*width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            neighbors = count_neighbors(board, x, y)
            if board[y][x] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_board[y][x] = 1
            else:
                if neighbors == 3:
                    new_board[y][x] = 1
    return new_board


CELL_SIZE = 20
screen_width = width * CELL_SIZE
screen_height = height * CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()

running = True
paused = True
generation = 0

while running:
    screen.fill((10, 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:               
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:   # Space button = Pause/Unpause
                paused = not paused
            elif event.key == pygame.K_n:     #  Button N = Single step
                if paused:
                  board = next_gen(board)
                  generation += 1
            elif event.key == pygame.K_r:
                board = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]   # Button R = Random
            elif event.key == pygame.K_c:                         # Button C = Clear
                board = [[0]*width for _ in range(height)]
            elif event.key == pygame.K_s:                      # Button S = Save
                save_pattern(board)
            elif event.key == pygame.K_l:                      # Button L = Load
                board = load_pattern()

    if not paused:
        board = next_gen(board)
        generation += 1

    # Draw live cells
    for y in range(height):
        for x in range(width):
            if board[y][x] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1))

    pygame.display.flip()
    clock.tick(args.fps)

pygame.quit()

def save_pattern(board, filename='patterns.txt'):
    with open(filename, 'w') as f:
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 1:
                    f.write(f"{x},{y}\n")

def load_pattern(filename='patterns.txt'):
    new_board = [[0]*width for _ in range(height)]
    try:
        with open(filename, 'r') as f:
            for line in f:
                x, y = map(int, line.strip().split(','))
                new_board[y][x] = 1
    except FileNotFoundError:
        print("Pattern file not found.")
    return new_board

