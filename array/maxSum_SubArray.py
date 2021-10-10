"""
There are several ways to do it
"""
from typing import List

"""
Way 1:  BRUTEFORCE:  O(n^2)

nums = [-2, 1, 3, 4, -1, 2, 1, -5, 4]
i        0  1  2  3  4   5  6   7  8
j           0  1  2  3   4  5   6  7 ==> find max() *--*
j              0  1  2   3  4   5  6 ==> find max()    |
j                 0  1   2  3   4  5 ==> find max()    |
j                    0   1  2   3  4 ==> find max()    |
j                        0  1   2  3 ==> find max()    *---- max from all
j                           0   1  2 ==> find max()    |     of these
j                               0  1 ==> find max()    |
j                                  0 ==> find max() *--*
"""
def bruteForce(nums: List[int]) -> int:
    tot = 0
    for i in range(len(nums)):
        subtot = 0
        for j in range(i + 1, len(nums)):
            subtot += nums[j]
            tot = max(tot, subtot)
    return tot


print("")
print("*** BRUTE FORCE ***")
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(bruteForce(nums))     #OUTPUT: 6
nums = [-2, 1, 3, 4, -1, 2, 1, -5, 4]
print(bruteForce(nums))     #OUTPUT: 10
print("")



"""
Way 2:  BETTER, but if we still don't care about what the subarray is
        O(n)
"""
def maxSum_SubArray(nums):
    tot = nums[0]
    subtot = 0

    for n in nums:
        if subtot < 0:
            subtot = 0
        subtot += n
        tot = max(tot, subtot)   #This the key!
    return tot


print("")
print("*** BETTER WAY ***")
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSum_SubArray(nums))     #OUTPUT: 6
nums = [-2, 1, 3, 4, -1, 2, 1, -5, 4]
print(maxSum_SubArray(nums))     #OUTPUT: 10
print("")



"""
Way 3: Using Kadane's method - If we care about what they are
    O(n)
"""
def kadane(nums):
    tot, subtot = 0, 0
    start, end = 0, 0

    for i in (range(len(nums))):
        subtot = subtot + nums[i]
        if tot < subtot:
            tot = subtot
            end = i
        if subtot < 0:
            subtot = 0
            start = i + 1    # start will begin in the next one (i+1)
    return tot, start, end


print("")
print("*** KADANE WAY ***")
# i      0  1  2  3  4   5  6   7  8
nums = [-2, 1, 3, 4, -1, 2, 1, -5, 4]
maxSum, start, end = kadane(nums)
print(f"MaxSum = {maxSum} ::: start pos = {start} ::: end pos = {end}")
print("[", end="")
for j in range(start, end+1):
    print(nums[j], end=",")
print("]", end="")
"""
             i       0     1  2  3   4  5   6    7    8
                   [-2,    1, 3, 4, -1, 2,  1,  -5,   4]
                   -------------------------------------
curSum       0      -2->0  1  4  8   7  9  10    5    9   
maxSub      -2             1  4  8   8  9  10   10  [10]
start        0             1  1  1      1  [1]  
end          0             1  2  2      5  [6]
ptr          0       1      

Output:
MaxSum = 10 ::: start pos = 1 ::: end pos = 6
[1,3,4,-1,2,1,]
"""

print("\n")
# i      0  1  2  3  4   5  6   7  8
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum, start, end = kadane(nums)
print(f"MaxSum = {maxSum} ::: start pos = {start} ::: end pos = {end}")
print("[", end="")
for j in range(start, end+1):
    print(nums[j], end=",")
print("]", end="")
""" 
             i       0     1   2     3   4  5   6    7    8
                   [-2,    1, -3,    4, -1, 2,  1,  -5,   4]
                   -----------------------------------------
curSum       0      -2->0  1  -2->0  4   3  5   6    1    5 
maxSub      -2             1   1     4   4  5   6    6   [6]
start        0             1         3      3  [3]
end          0             1         3      5  [6]
ptr          0       1        3

Output:
MaxSum = 6 ::: start pos = 3 ::: end pos = 6
[4,-1,2,1,]
"""