'''
Leetcode 55:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

index:   0  1  2  3  4  5  6  7  8  9
        [1, 1, 2, 5, 2, 1, 0, 0, 1, 3]

The frog can jump from 0 .. n steps (as indicated in the value of each element in the array)
So, we need to find the MAX value after jumping 0->n steps on each step(index i)

index 0:    0+1 = 1  ...  reachable = max(0, 1) -> 1
      1:    1+1 = 2  ...  reachable = max(1, 2) -> 2
      2:    2+2 = 4  ...  reachable = max(2, 4) -> 4
      3:    3+5 = 8  ...  reachable = max(4, 8) -> 8
      4:    4+2 = 6  ...  reachable = max(8, 6) -> 8
      5:    5+1 = 6  ...  reachable = max(8, 6) -> 8
      6:    6+0 = 6  ...  reachable = max(8, 6) -> 8
      7:    7+0 = 7  ...  reachable = max(8, 7) -> 8
      8:    8+1 = 9  ...  reachable = max(8, 9) -> 9
      9:    9+3 = 12 ...  reachable = max(9,12) -> 12

Fail testcase:
index:   0  1  2  3  4  5  6  7  8  9
        [1, 1, 2, 5, 2, 1, 0, 0, 0, 3]

The frog can jump from 0 .. n steps (as indicated in the value of each element in the array)
So, we need to find the MAX value after jumping 0->n steps on each step(index i)

index 0:    0+1 = 1  ...  reachable = max(0, 1) -> 1
      1:    1+1 = 2  ...  reachable = max(1, 2) -> 2
      2:    2+2 = 4  ...  reachable = max(2, 4) -> 4
      3:    3+5 = 8  ...  reachable = max(4, 8) -> 8
      4:    4+2 = 6  ...  reachable = max(8, 6) -> 8
      5:    5+1 = 6  ...  reachable = max(8, 6) -> 8
      6:    6+0 = 6  ...  reachable = max(8, 6) -> 8
      7:    7+0 = 7  ...  reachable = max(8, 7) -> 8
      8:    8+0 = 8  ...  reachable = max(8, 8) -> 8  <-> here reachable is not < i
      9:    FAIL
'''

class Frog:
    def canJump(self, array):
        reachable = 0
        for i in range(len(array)):
            if (reachable < i):     ## this means unable to reach destination
                return False
            else:
                reachable = max(reachable, i + array[i])
                print(i, reachable)
        return True


if __name__ == '__main__':
    frog = Frog()
    array = [1,1,2,5,2,1,0,0,1,3]
    print("Can the frog reach the destination: ", end='')
    print(frog.canJump(array))

    array = [1, 1, 2, 5, 2, 1, 0, 0, 0, 3]
    print("Can the frog reach the destination: ", end='')
    print(frog.canJump(array))
