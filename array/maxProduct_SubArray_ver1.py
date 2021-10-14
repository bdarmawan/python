def maxProdSubarray(nums):
    currMaxProduct = nums[0]
    currMinProduct = nums[0]
    prevMaxProduct = nums[0]
    prevMinProduct = nums[0]
    ans = nums[0]

    for i in range(1, len(nums)):
        currMaxProduct = max(prevMaxProduct * nums[i], prevMinProduct * nums[i], nums[i])
        currMinProduct = min(prevMaxProduct * nums[i], prevMinProduct * nums[i], nums[i])
        if i > 1:
            ans = max(ans, currMaxProduct)
        else:
            anx = max(currMaxProduct, currMinProduct)
        prevMaxProduct = currMaxProduct
        prevMinProduct = currMinProduct
    return ans


nums = [1,2,-3,0,6,7]
print(f"Array: {nums}")
print(maxProdSubarray(nums))        #OUTPUT: 42

nums = [1,2,-3,1,-6,7]
print(f"Array: {nums}")
print(maxProdSubarray(nums))        #OUTPUT: 252

nums = [1,2,-3,1,6,7]
print(f"Array: {nums}")
print(maxProdSubarray(nums))        #OUTPUT: 42

nums = [1,2,-3,0,6,-5]
print(f"Array: {nums}")
print(maxProdSubarray(nums))        #OUTPUT: 6

"""
Array:        [1, 2,                   -3,                     0,  .................]
    currMax    1  max(1*2, 1*2, 2)=2   max(2*-3, 2*-3, -3)=-3  max(-3*0, -6*0, 0)=0
    currMin    1  min(1*2, 1*2, 2)=2   min(x*-3, 2*-3, -3)=-6  min(-3*0, -6*0, 0)=0
    ans        1  max(2,2)=2           max(-3,-6)=-3           max(0,0)=0
    prevMax    1  2                    -3                      0
    prevMin    1  2                    -6                      0
    
Array:        [6,                      7]
    currMax    max(0*6, 0*6, 6)=6      max(6*7, 6*7, 7)=42  
    currMin    min(0*6, 0*6, 6)=6      min(6*7, 6*7, 7)=7   
    ans        max(6,6)=6              max(42,7)=42          
    prevMax    6                       42                      
    prevMin    6                       7                      

Array: [1, 2, -3, 0, 6, 7]
42

Array: [1, 2, -3, 1, -6, 7]
252

Array: [1, 2, -3, 1, 6, 7]
42

Array: [1, 2, -3, 0, 6, -5]
0
"""