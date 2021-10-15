def findMissingNumberBruteForce(myArray: list) -> int:
    # Brute Force
    """
             1  2  3  4  5  6  7
    cnt      1  0  1  1  0  0  1
    """

    # Find max element
    biggest = max(myArray) + 1
    arr = [0] * biggest
    for j in myArray:
        arr[j] = 1

    for i in range(1, len(arr)):
        if arr[i] == 0:
           missingNumber = i
           return missingNumber



def findMissingNumber(nums: list) -> int:
    n = len(nums)
    for i in range(n):
       correctPos = nums[i] - 1 # number 3 goes to index 2
       while 1 <= nums[i] <= n  and  nums[i] != nums[correctPos]:
          print(f"Swap: nums[{i}] with nums[{correctPos}]")
          nums[i], nums[correctPos] = nums[correctPos], nums[i]   # swap
          print(nums)
          correctPos = nums[i] - 1

    for i in range(n):
        if i+1 != nums[i]:
            return i+1
    return n+1



myArray = [3, 4, 7, 1]
print(findMissingNumberBruteForce(myArray))     #OUTPUT: 2

print("***************************************************")
print(findMissingNumber(myArray))               #OUTPUT: 2

"""
Output:
2
***************************************************
Original:
[3, 4, 7, 1]
Swap: nums[0] with nums[2]
[7, 4, 3, 1]
Swap: nums[1] with nums[3]
[7, 1, 3, 4]
Swap: nums[1] with nums[0]
[1, 7, 3, 4]
2
"""