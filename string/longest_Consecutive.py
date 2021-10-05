from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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

"""
List: [100, 4, 200, 1, 3, 2]
Longest consecutive: 4  ---> which is 1,2,3,4
"""