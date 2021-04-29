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

#        0  1  2  3  4   5  6   7  8
nums = [-2, 1, 3, 4, -1, 2, 1, -5, 4]
maxSum, start, end = maxSum_SubArray2(nums)
print(f"MaxSum = {maxSum} ::: start pos = {start} ::: end pos = {end}")
print("[", end="")
for j in range(start, end+1):
    print(nums[j], end=",")
print("]", end="")
"""
  0  1  2  3   4  5  6   7  8
[-2, 1, 3, 4, -1, 2, 1, -5, 4]
MaxSum = 10 ::: start pos = 1 ::: end pos = 6
[1,3,4,-1,2,1,]
"""