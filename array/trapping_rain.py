'''
arr = [3,0,2,0,4]

            x
    x       x
    x   x   x          OUTPUT: 7
    x   x   x
    -------------------
'''


def rainTrap(arr):
    numWater = 0
    for i in range(1, len(arr)):     # arr[0] is always 0
        maxLeft  = max(arr[:i])      # since it won't be able to collect water
        maxRight = max(arr[i:])
        waterToCollect = min(maxLeft, maxRight) - arr[i]   # remember need - arr[i]
        if waterToCollect < 0:  waterToCollect = 0
        print(i, arr[i], maxLeft, maxRight, waterToCollect)
        numWater += waterToCollect
    print(f"Number of collected water: {numWater}")


if __name__ == "__main__":
    arr = [3,0,2,0,4]
    rainTrap(arr)   # OUTPUT: 7

    arr = [2,0,2]
    rainTrap(arr)   # OUTPUT: 2

    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    rainTrap(arr)   # OUTPUT: 6

    arr = []
    rainTrap(arr)   # OUTPUT: 0

    arr = [1,1,1,1,1]
    rainTrap(arr)   # OUTPUT: 0

    arr = [1,-1,-2]
    rainTrap(arr)   # OUTPUT: 0
'''
1 0 3 4 3
2 2 3 4 1
3 0 3 4 3
4 4 3 4 0
Number of collected water: 7
1 0 2 2 2
2 2 2 2 0
Number of collected water: 2
1 1 0 3 0
2 0 1 3 1
3 2 1 3 0
4 1 2 3 1
5 0 2 3 2
6 1 2 3 1
7 3 2 3 0
8 2 3 2 0
9 1 3 2 1
10 2 3 2 0
11 1 3 1 0
Number of collected water: 6
'''