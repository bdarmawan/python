###
### There are 2 WAYS
###

def rotateArray1(arrays, k):
    ### 1 2 3 4 5 6 7 8
    ### 8 7 6 5 4 3 2 1
    ### <-k->|<-------->
    ### 6 7 8|1 2 3 4 5
    rArray = sorted(arrays, reverse=True)
    sub1 = rArray[:k]
    sub2 = rArray[k:]
    return sorted(sub1) + sorted(sub2)

def rotateArray2(arrays, k):
    ### 1 2 3 4 5 6 7 8
    ### <---k---> 1 2 3
    ### 4 5 6 7 8
    ### (i + k) % n
    n = len(arrays)
    newArray = [0] * n
    for i in range(len(arrays)):
        newArray[i] = array[(i + n-k) % n]
    return newArray


###
###TEST

array = [1,2,3,4,5,6,7,8]
k = 3
print(rotateArray1(array, k))   #OUTPUT: [6, 7, 8, 1, 2, 3, 4, 5]
print(rotateArray2(array, k))   #OUTPUT: [6, 7, 8, 1, 2, 3, 4, 5]

