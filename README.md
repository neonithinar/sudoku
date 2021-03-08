# Sudoku
Sudoku puzzle solver app that can identify the sudoku puzzle from the given image file and solves the puzzle

**Frameworks used**
* Image identification and puzzle extraction: OpenCV 
* Image processing to puzzle matrix: Tensorflow-keras based neural network model (99.8% accuracy in MNIST dataset)
* Sudoku solver engine: Backtracking algorithm

### Puzzle extraction:
  Puzzle is extracted from the given noisy image and sliced to puzzle square using openCV operations like adaptive thresholding, prespective transformations and identifying largest contours
  < Add images >
  Image is sliced and indexed into the 81 small squares
  
  These images are fed into a pretrained neural network model trained on the MNIST dataset (99.8% test accuracy) to identify each of the digits in the image
  
  Puzzle board is extracted into a matrix and fed into the backtracking algorithm.
  
  ### Solving the puzzle
  Backtracking is a simple to implement and robust algorithm to solve sudoku puzzles of any difficulty. The algorithm works by going through all the empty cells in the puzzle from top-left to bottom-right corner. filling them up with possible correct digit insertions by checking the row, column and the square for possible mismatches. If the insert was found to conflict with any previous insertion, the algorithm back-tracks its steps to that step and continues to solve the puzzle after inserting the conflicted cell with a next possible match. After solving the puzzle final result is displayed
  
 [Backtracking in action](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Sudoku_solved_by_bactracking.gif/260px-Sudoku_solved_by_bactracking.gif)
 
 For more info on backtracking, click [here...](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms)
