#######################################
# 1 - Brute Force Without Memoization

# m = #row
# n = #column
# O(2 ^ (m + n)) time
# O(m + n) space
#######################################
def gridTraveler(row, col):
    if row == 1 and col == 1: return 1
    if row == 0  or col == 0: return 0

    return gridTraveler(row - 1, col) + gridTraveler(row, col - 1)


#######################################
# 2 - With Memoization

# O(m * n) time
# O(m + n) space
#######################################
def gridTravelerMemo(row, col, memo={}):
    key = str(row) + "," + str(col)

    if key in memo: return memo[key]
    if row == 1 and col == 1: return 1
    if row == 0  or col == 0: return 0

    memo[key] = gridTravelerMemo(row - 1, col, memo) + gridTravelerMemo(row, col - 1, memo)
    return memo[key]



#######################################
# 3 - With Tabulation

# O(m * n) time
# O(m * n) space
#######################################
def gridTravelerTab(row, col):
    table = [[0 for col in range(col + 1)] for row in range(row + 1)]  # tricky !!!
    # you can't do:     tab = [[0] * col] * row
    table[1][1] = 1
    for i in range(row + 1):
        for j in range(col + 1):
            current = table[i][j]
            if j+1 <= col: table[i][j+1] += current
            if i+1 <= row: table[i+1][j] += current
    return table[row][col]




## TEST ##
#####
# 1 #
#####
print(gridTraveler(1,1))    # 1
print(gridTraveler(2,3))    # 3
print(gridTraveler(3,2))    # 3
print(gridTraveler(3,3))    # 6
# Below will hang - b/c process too long - we need to memoize it
# print(gridTraveler(18,18))
print("")

#####
# 2 #
#####
print(gridTravelerMemo(1,1,{}))     # 1
print(gridTravelerMemo(2,3,{}))     # 3
print(gridTravelerMemo(3,2,{}))     # 3
print(gridTravelerMemo(3,3,{}))     # 6
print(gridTravelerMemo(18,18,{}))   # 2333606220
print("")

#####
# 3 #
#####
print(gridTravelerTab(1,1))     # 1
print(gridTravelerTab(2,3))     # 3
print(gridTravelerTab(3,2))     # 3
print(gridTravelerTab(3,3))     # 6
print(gridTravelerTab(18,18))   # 2333606220
