# Sudoku-Solver

The goal of this program is to automatically solve a Sudoku. 
The Sudoku is provided as a nested list of rows, where each row contains a list of numbers from 0 to 9. Every 0 is then replaced by an empty dictionary. 
In the next steps, the dictionary is updated with 'number: False' if the number is already present in the same row, column or 3x3 square. 

After all dictionaries are updated, all dictionaries with eight entries (8x False) with the remaining number. This cyclce is repeated until the Sudoku is solved or a maximum amount of iterations has passed.
