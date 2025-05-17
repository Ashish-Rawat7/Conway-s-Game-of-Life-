Conway's Game of Life – Interactive Visualizer
This project is a graphical simulation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. It provides an interactive environment using Python and Pygame, where users can start, pause, randomize, and control the evolution of cells on a 2D grid.

* Features
* Start/Pause the simulation with the spacebar.

* Click R to randomly generate cell patterns.

* Click S to save current pattern to a file.

* Click L to load a previously saved pattern.

* Click C to Clear the board.

* Click N to step through the simulation one generation at a time.


--Rules of the Game
    # Each cell in the grid is either alive (1) or dead (0) and updates based on its 8 neighbors:

   # Any live cell with fewer than two live neighbors dies (underpopulation).

   # Any live cell with two or three live neighbors lives on.

   # Any live cell with more than three live neighbors dies (overpopulation).

  # Any dead cell with exactly three live neighbors becomes a live cell (reproduction).


--Install Dependencies--
  1. Make sure Python is installed. Then install pygame:
    # pip install pygame

 2. Run the Simulation
   #python game_of_life.py --width 60 --height 30 --fps 10
    You can customize the board size and frame rate using CLI arguments.

  
