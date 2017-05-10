Backtracking Depth First Search : Sudoku Solver
--------------
  This project aims to implement Depth First Search algorithm with backtracking property.
It is simple and straightforward code that takes significant time to terminate, thus solve the puzzle.
Since the time complexity of DFS is O(b^d) in worst case.
  printBoard takes the sudoku board and prints it.
  isFull takes the sudoku board and check if it is all filled.
  possibleEntries takes sudoku board, cell row(i) and column(j) number and returns a dictionary with the possible numbers that (i,j) cell can take.

File list
------------
sudoku.py   all functions and solving happens here.
README			This file

Prerequisities
--------------
example: Python version 2.7 or later releases

Running
--------------
1. Save all Python source files in one same directory. Let's call it "project_source"
2. From terminal change directory to project_source.
3. Run the main script:
	>> python sudoku.py

* sudoku layout can be changed in source code

Authors
-------------
Caner Eren
Hatice Yüksel
