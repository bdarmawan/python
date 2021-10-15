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



### 2ND BEST, but there is a chance of getting overflow if the numbers are too big
###
### If the numbers ARE in sequennce, for example: [3,0,1] as in 0,1,2,3
###                                       with 2 is the missing number
### Then you can use math:  n * (n-1)/2 - sum[]
def findMissingNumberWithMath(nums: list) -> int:
    tot = 0
    for num in nums:
        tot += num
    n = len(nums)
    return int((n+1) * n/2 - tot)



### 1st BEST, NO OVERFLOW
###
### If the numbers ARE in sequennce, for example: [3,0,1] as in 0,1,2,3
###                                       with 2 is the missing number
### Then you can XOR Operation
###      (1 ^ 2 ^ 3 ^ 4 ^ 5)  ^  (1 ^ 2  ^ 4 ^ 5) = 3
def findMissingNumberWithXOR(nums: list) -> int:
    x = nums[0]
    for i in range(1, len(nums)):
        x ^= nums[i]                    # 3 ^ 4 ^ 6 = 1

    xmin, xmax = min(nums), max(nums)
    y = xmin
    for i in range(xmin+1, xmax+1):
        y ^= i                          # 3 ^ 4 ^ 5 ^ 6 = 4
    return x ^ y                        # 1 ^ 4 = 5




def findMissingNumberBySwapping(nums: list) -> int:
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


###
###TEST
myArray = [3, 4, 7, 1]
print(findMissingNumberBruteForce(myArray))     #OUTPUT: 2

print("***************************************************")
myArray = [3, 4, 7, 1]
print(findMissingNumberBySwapping(myArray))               #OUTPUT: 2

print("***************************************************")
myArray = [3,0,1]
print(findMissingNumberWithMath(myArray))       #OUTPUT: 2

print("***************************************************")
myArray = [3,4,6]
print(findMissingNumberWithXOR(myArray))       #OUTPUT: 5

print("***************************************************")
myArray = [3,4,5,6,8]
print(findMissingNumberWithXOR(myArray))       #OUTPUT: 7

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