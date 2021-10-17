###
### Choice 1
### BRUTE FORCE
def maxSubSequenceBF(nums):
    tot = 0
    for num in nums:
        if num > 0:     # since we're finding maxSum, thus only consider +'ve numbers only
           tot += num
    return tot



###
### Choice 2
def maxSubSequence2(nums):
    subtot, subMax = 0, 0

    for num in nums:
        subtot += num
        subMax = max(subMax, subtot, num)
        subtot = subMax
    return subMax


###
### Choice 3
def maxSubSequence(myList):
    maxRun = 0
    maxSum = 0
    for i in myList:
        curSum = i + maxSum
        maxRun = max(maxRun, curSum)
        print(i, curSum, maxSum, end=" => ")
        maxSum = max(curSum, maxRun, i)
        print(maxSum)
    return maxSum


###
### TEST
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"List: {a}")
print(f"MaxSum: {maxSubSequence(a)}")           #OUTPUT: 12
print(f"MaxSum: {maxSubSequence2(a)}")          #OUTPUT: 12
print(f'MaxSum BF: {maxSubSequenceBF(a)}')      #OUTPUT: 12
print("")
"""
           *      *      *  *      *
List: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
   i   curSum  maxRun    maxSum
  -2     -2      0    =>    0
   1      1      0    =>    1
  -3     -2      1    =>    1
   4      5      1    =>    5
  -1      4      5    =>    5
   2      7      5    =>    7
   1      8      7    =>    8
  -5      3      8    =>    8
   4     12      8    =>   12
MaxSum: 12
"""

b = [-2, 1, -3, 4, -1, 2, 1, 5, 4]
print(f"List: {b}")
print(f"MaxSum: {maxSubSequence(b)}")           #OUTPUT: 17
print(f"MaxSum: {maxSubSequence2(b)}")          #OUTPUT: 17
print(f'MaxSum BF: {maxSubSequenceBF(b)}')      #OUTPUT: 17
"""
           *      *      *  *  *  *
List: [-2, 1, -3, 4, -1, 2, 1, 5, 4]
   i   curSum  maxRun    maxSum
  -2     -2      0    =>    0
   1      1      0    =>    1
  -3     -2      1    =>    1
   4      5      1    =>    5
  -1      4      5    =>    5
   2      7      5    =>    7
   1      8      7    =>    8
   5     13      8    =>   13
   4     17     13    =>   17
MaxSum: 17
"""

# Think to consider
# To get max Sum of SubSequence, can we just take all the postive numbers?