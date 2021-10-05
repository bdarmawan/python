from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        total = 0
        for num in nums:
            if num in s:
                total -= num
            else:
                s.add(num)
                total += num
        return total


###
### TEST
s = Solution()
nums = [2,2,1]
print(s.singleNumber(nums))  # OUTPUT: 1
nums = [4,1,2,1,2]
print(s.singleNumber(nums))  # OUTPUT: 4
nums = [1]
print(s.singleNumber(nums))  # OUTPUT: 1
nums = []
print(s.singleNumber(nums))  # OUTPUT: 0
nums = [-2,-2,1]
print(s.singleNumber(nums))  # OUTPUT: 1
nums = [-2,-2,1,2,2]
print(s.singleNumber(nums))  # OUTPUT: 1
