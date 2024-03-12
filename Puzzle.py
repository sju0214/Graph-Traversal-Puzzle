def solve_puzzle(Board, Source, Destination):
    # initialize queue with Source
    queue = [(Source, [Source])]
    visited = set([Source])

    while queue: 
        (cell, path) = queue.pop(0)
        # if the current cell matches the Destination, then return path
        if cell == Destination: 
            return path
        
        for direction in [(0,1), (0, -1), (1, 0), (-1,0)]:
            next = (cell[0] + direction[0], cell[1] + direction[1])
            if (0 <= next[0] < len(Board) and 0 <= next[1] < len(Board[0])):
                # if the next cell is not an obstacle and has not been visted
                if (Board[next[0]][next[1]] != '#' and next not in visited):
                    # add to queue and mark as visited
                    queue.append((next, path + [next]))
                    visited.add(next)
