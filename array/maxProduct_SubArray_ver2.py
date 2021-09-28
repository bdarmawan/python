def maxProduct(nums):
    res = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:
            curMin, curMax = 1,1
            continue
        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res


"""
This one below seems to be better
"""
def maxProduct2(nums):
    curr_max_product = nums[0]   # initial all max with first element of the array
    prev_max_product = nums[0]
    prev_min_product = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):  # note that we start the loop from the 2nd element
        curr_max_product = max(prev_max_product * nums[i], prev_min_product * nums[i], nums[i])
        curr_min_product = min(prev_max_product * nums[i], prev_min_product * nums[i], nums[i])
        res = max(res, curr_max_product)
        prev_max_product = curr_max_product
        prev_min_product = curr_min_product
    return res


### All positive
nums = [1, 2, 3]
print(maxProduct(nums))    #6

### All Negative
nums = [-1, -2, -3]
print(maxProduct(nums))    #6

### Combination
nums = [-1, 2, -3]
print(maxProduct(nums))    #6

### Combination
nums = [-1, 2, -3, -4]
print(maxProduct(nums))    #24

### Combination
nums = [0, 2, -3, -4]
print(maxProduct(nums))    #24

"""
Using second method
"""
print()
### All positive
nums = [1, 2, 3]
print(maxProduct2(nums))    #6

### All Negative
nums = [-1, -2, -3]
print(maxProduct2(nums))    #6

### Combination
nums = [-1, 2, -3]
print(maxProduct2(nums))    #6

### Combination
nums = [-1, 2, -3, -4]
print(maxProduct2(nums))    #24

### Combination
nums = [0, 2, -3, -4]
print(maxProduct2(nums))    #24

### Combination
nums = [1, 2, 0, -3, -4]
print(maxProduct2(nums))    #12