# Graph Traversal to Solve Puzzle

### Overview 

Given a 2-D puzzle of size MxN with N rows and M column and two coordinates from
the puzzle (a,b) and (x,y), the goal is to reach (x,y) from the location (a, b).
Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by
‘-’ (hyphen) and the one with a barrier is marked by ‘#’. 

You can move only in the following directions:
L: move to left cell from the current cell
R: move to right cell from the current cell
U: move to upper cell from the current cell
D: move to the lower cell from the current cell

### Implementation Details
INPUT: board, source, destination.
- puzzle: A list of lists, each list represents a row in the rectangular puzzle. Each
  element is either ‘-’ for empty (passable) or ‘#’ for obstacle (impassable).
- source: A tuple representing the indices of the starting position
- destination: A tuple representing the indices of the goal position

OUTPUT: A list of tuples representing the indices of each position in the path. The first tuple should be the starting position, or source, and the last tuple should be the destination. If there is no valid path, None should be returned. Not an empty list, but the None object. If source and destination are same return the same cell.
