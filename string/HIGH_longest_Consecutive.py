from typing import List


class Solution:

###
### 1st Option
    def longestConsecutive(self, numbers: List[int]) -> int:
        numSet = set(numbers)   # convert to set to take care of duplicate element
        for num in numbers:
            if num - 1 not in numSet:
                length = 1
                while num + 1 in numSet:
                    length += 1
                    num += 1
        return length


###
### 2nd Option
    def longestConsecutive_v2(self, nums: List[int]) -> int:
        numSet = set(nums)
        # convert to set to take care of duplicate element
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


s = Solution()
b = [100, 4, 200, 1, 3, 2]
print(f"List: {b}")
print(f"Longest consecutive: {s.longestConsecutive(b)}")
print(f"Longest consecutive: {s.longestConsecutive_v2(b)}")

"""
List: [100, 4, 200, 1, 3, 2]
Longest consecutive: 4  ---> which is 1,2,3,4
"""