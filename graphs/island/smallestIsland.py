import math

def minIsland(grid):
    visited = set()
    minSize = math.inf

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore(grid, r, c, visited)
            if (size > 0 and size < minSize):    # Tricky on size > 0 - consider only island
                minSize =  size                  # ... there is no island's size = 0
    return minSize


def explore(grid, r, c, visited):
    rowInbounds = 0 <= r and r < len(grid)      # pay attention to  <=  and  <
    colInbounds = 0 <= c and c < len(grid[0])

    #BASE CASE
    if not rowInbounds or not colInbounds: return False
    if grid[r][c] == "W": return 0

    pos = str(r) + ',' + str(c)
    if pos in visited: return 0
    visited.add(pos)

    #EXPLORE NEIGHBORS
    size = 1
    size += explore(grid, r-1, c, visited)
    size += explore(grid, r+1, c, visited)
    size += explore(grid, r, c-1, visited)
    size += explore(grid, r, c+1, visited)
    return size





grid = [
    ['W', 'L', 'W', 'L', 'W'],
    ['L', 'L', 'W', 'L', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['W', 'W', 'L', 'W', 'W'],
]

print(minIsland(grid))