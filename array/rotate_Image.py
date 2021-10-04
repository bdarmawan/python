from typing import List
'''
          -------> IV
           L           R
 I    T  [ 5   1   9  11]    |              [15  13   2   5]
 ^       [ 2   4   8  10]    |              [14   3   4   1]
 |       [13   3   6   7]    v              [12   6   8   9]
 |    B  [15  14  12  16]   III             [16   7  10  11]
          
          <------ II

'''
arr = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

def rotate(arr: List[List[int]]) -> None:
    l, r = 0, len(arr) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            topLeft = arr[top][l + i]           #save topLeft
            arr[top][l + i] = arr[bottom - i][l]        #I - move Bottom Left to Top Left
            arr[bottom - i][l] = arr[bottom][r - i]     #II - move Bottom Right to Bottom Left
            arr[bottom][r - i] = arr[top + i][r]        #III - move Top Right to Bottom Right
            arr[top + i][r] = topLeft                   #IV - move Top Left to Top Right
        r -= 1
        l += 1

    print(f"New Array: {arr}")


###
###TEST
print(f"Old Array: {arr}")
rotate(arr)