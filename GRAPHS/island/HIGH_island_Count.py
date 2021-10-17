def islandCount(grid):
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True: count += 1
    return count


def explore(grid, r, c, visited):
    rowInbounds = 0 <= r and r < len(grid)      # pay attention to  <=  and  <
    colInbounds = 0 <= c and c < len(grid[0])

    #BASE CASE
    if rowInbounds == False or colInbounds == False: return False   # This order is important
    if grid[r][c] == "W": return False                              # if you don't check the inbounds this line
                                                                    # will be giving out index out of bound

    pos = str(r) + ',' + str(c)
    if pos in visited: return False
    visited.add(pos)

    #EXPLORE NEIGHBORS
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r, c+1, visited)
    return True





grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

print(islandCount(grid))      # OUTPUT: 3