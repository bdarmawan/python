#Dynamic Programming


# 1ST CHOICE
def LIS(nums):
    LIS = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]  and  LIS[i] <= LIS[j]:
                LIS[i] = 1 + LIS[j]

    print(f'Array: {nums}')
    print(LIS)
    return max(LIS)


### DP
def lengthOfLIS(nums):
    LIS = [1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1+LIS[j])

    return max(LIS)


myList = [1,2,4,3]
print(f"Longest increasing subsequence of {myList} is {lengthOfLIS(myList)}")       #OUTPUT: 3

myList = [1,2,4,3]
print(LIS(myList))      #OUTPUT: 3


"""
Output:
Longest increasing subsequence of [1, 2, 4, 3] is 3

 0  1  2  3
[1, 2, 4, 3]
                                              ROOT
                                                |
                            ------------------------------------------
                         0  |          1   |         2  |           3  |
                           [1]            [2]          [4]           [3]
                            |
                   ------------------
                 1 |       2 |       3 |         
                 [1,2]    [1,4]   [1,3]
                   |
              ----------     
            2 |      3 |
          [1,2,4]   [1,2,3]

LIS[3] = 1

LIS[2] = max(1, 1 + LIS[3])
       = max(1, x) -> LIS[3] in this example is not allowed b/c nums[2] is > nums[3]
                                                    that is it's not inceasing order
       = 1
       
LIS[1] = max(1,  1 + LIS[2],  1 + LIS[3])
        = max(1, 1+1,  1+1) = max(1, 2, 2) 
        = 2

LIS[0] = max(1,  1 + LIS[1],  1 + LIS[2],  1 + LIS[3])
       = max(1, 1+2,  1+1,  1+1) = max(1, 3, 2, 2) 
       = 3
"""