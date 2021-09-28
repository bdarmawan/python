"""
If we care about what they are
"""
def maxSum_SubArray(nums):
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub


"""
Using Kadane's method
If we care about what they are
"""
def maxSum_SubArray2(nums):
    maxSub = nums[0]
    curSum = 0
    start, end, ptr = 0, 0, 0
    for i in (range(len(nums))):
        curSum = curSum + nums[i]
        if maxSub < curSum:
            maxSub = curSum
            start, end = ptr, i
        if curSum < 0:
            curSum = 0
            ptr = i + 1
    return maxSub, start, end



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSum_SubArray(nums))     # 6
nums = [-2, 1, 3, 4, -1, 2, 1, -5, 4]
print(maxSum_SubArray(nums))     # 10

"""
Output:
6
10
"""
#        0  1  2  3  4   5  6   7  8
nums = [-2, 1, 3, 4, -1, 2, 1, -5, 4]
maxSum, start, end = maxSum_SubArray2(nums)
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
-----
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