def numIslands(grid):
    num = 0
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                check_visited(grid, row, col, i, j)
                num += 1
    return num



def check_visited(grid, row, col, x, y):
    # check out of boundary
    # also check if the cell is an island (== 1)
    if (x < 0) or (x >= row) or (y < 0) or (y >= col) or (grid[x][y] != "1"):
        return

    # mark the cell as visited (2)
    grid[x][y] = "2"

    check_visited(grid, row, col, x+1, y)     # DOWN
    check_visited(grid, row, col, x,   y+1)   # RIGHT
    check_visited(grid, row, col, x-1, y)     # UP
    check_visited(grid, row, col, x,   y-1)   # LEFT



grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

grid2 = [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]

print(numIslands(grid))
print(numIslands(grid2))
