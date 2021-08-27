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


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"List: {a}")
print(f"MaxSum: {maxSubSequence(a)}")

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
print(f"MaxSum: {maxSubSequence(b)}")
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