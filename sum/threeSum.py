from typing import List

"""
Find 3 combination that gives sum == 0

[3, 5, 1, -4, 10, 1] -> sorted: [-4, 1, 1, 3, 5, 10]

    [-4, 1, 1, 3, 5, 10]
      i
         l<-- like --> r
           binary tree
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(f"Sorted nums: {nums}")   # Sorted nums: [-4, 1, 1, 3, 5, 10]

        for i, a in enumerate(nums):
            if i > 0  and  a == nums[i-1]:
                continue   # skip if there's a repetition in nums

            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1      # reduce the right pointer
                elif threeSum < 0:
                    l += 1      # increase the left pointer
                else:
                    # find the answer
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1]:
                        # this is to avoid repeating answer
                        # without this the result is:
                        # [[-4, 1, 3], [-4, 1, 3]]
                        # because Sorted nums: [-4, 1, 1, 3, 5, 10]
                        #                           ^  ^
                        l += 1
        return res


s = Solution()
arr = [3, 5, 1, -4, 10, 1]
print(arr)
print(f"Result: {s.threeSum(arr)}")

"""
[3, 5, 1, -4, 10, 1]
Sorted nums: [-4, 1, 1, 3, 5, 10]
Result: [[-4, 1, 3]]
"""