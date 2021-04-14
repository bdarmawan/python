def sortedSquare(arr):
    """

     [-12, -4, -1, 0, 3, 10, 30]
        ^                     ^
        |                     |
      left                   right


[-12, -4, -1, 0, 3, 10, 30]
  ^                      ^
                          [0, 0, 0, 0, 0, 0, 900]
[-12, -4, -1, 0, 3, 10, 30]
  ^                 ^
                          [0, 0, 0, 0, 0, 144, 900]
[-12, -4, -1, 0, 3, 10, 30]
       ^            ^
                          [0, 0, 0, 0, 100, 144, 900]
[-12, -4, -1, 0, 3, 10, 30]
       ^         ^
                          [0, 0, 0, 16, 100, 144, 900]
[-12, -4, -1, 0, 3, 10, 30]
          ^      ^
                          [0, 0, 9, 16, 100, 144, 900]
[-12, -4, -1, 0, 3, 10, 30]
          ^   ^
                          [0, 1, 9, 16, 100, 144, 900]

     """

    left = 0
    right = len(arr)-1
    length = len(arr)
    newArr = list('0' * length)

    for i in range(length-1, 0, -1):
        if abs(arr[left]) > abs(arr[right]):
            newArr[i] = arr[left] ** 2
            left += 1
        else:
            newArr[i] = arr[right] ** 2
            right -= 1
    return newArr


arr = [-12, -4, -1, 0, 3, 10, 30]
print(sortedSquare(arr))

"""
output: ['0', 1, 9, 16, 100, 144, 900] 
"""