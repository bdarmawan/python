def prodArray(nums):
    """
    nums = [1, 2, 3, 4]
    multiplyAll = 1*2*3*4 = 24
    Now for each element, divide 24/nums[i]
    op   = [24/1, 24/2, 24/3, 24/4] -> [24, 12, 8, 6]
    O(n)
    """
    multiplyAll = 1
    res = [0] * len(nums)
    for i in range(len(nums)):
        multiplyAll *= nums[i]

    for i in range(len(nums)):
        if nums[i] == 0:
            res[i] = 0
        else:
            res[i] = int(multiplyAll/nums[i])

    return res


def prodArray2(nums):
    """
    if division operation is not allowed.
    nums  = [1,   2,  3,  4]
    left  = [1,   2,  6, 24]  ::: this is LeftToRight
    right = [24, 24, 12,  4]  ::: this is RightToLeft
    boundaryCase:
        * for i = 0   -> op[i] = right[1]
        * for i = n-1 -> op[i] = left[n-2]
    otherwise:
        * op[i] = left[i-1] * right[i+1]
    op    = [24, 1*12=12, 2*4=8, 6]
    O(n)
    """
    left  = [1] * len(nums)
    right = [1] * len(nums)
    res   = [1] * len(nums)

    n = len(nums)
    for i in range(n):
        if i == 0:
            left[i] = nums[i]
        else:
            left[i] = left[i-1] * nums[i]
    print(f"LEFT: {left}")

    for i in range(n-1, -1, -1):
        if i == n-1:
            right[i] = nums[i]
        else:
            right[i] = right[i+1] * nums[i]
    print(f"RIGHT: {right}")

    for i in range(0, n):
        if i == 0:
            res[i] = right[1]
        elif i == n-1:
            res[i] = left[n-2]
        else:
            res[i] = left[i-1] * right[i+1]
    return res


array = [1,2,3,4]
print(array)
print(prodArray(array))
print(prodArray2(array))

"""
[1, 2, 3, 4]
[24, 12, 8, 6]

LEFT: [1, 2, 6, 24]
RIGHT: [24, 24, 12, 4]
[24, 12, 8, 6]
"""