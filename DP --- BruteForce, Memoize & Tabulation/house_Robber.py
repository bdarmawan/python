from typing import List
''' 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that 
adjacent houses have security systems connected

     i: 0   1   2   3
        1   2   3   1
        
  i:0    1                                                  ===> dp[1, 0, 0, 0]
  i:1    max(nums[0], nums[1]) --> max(1,2) = 2             ===> dp[1, 2, 0, 0]
  i:2    max(nums[2] + dp[0], dp[1]) --> max(3+1, 2) = 4    ===> dp[1, 2, 4, 0]
  i:3    max(nums[3] + dp[1], dp[2]) --> max(1+2, 4) = 4    ===> dp[1, 2, 4, 4]
  
  dp[-1] = 4
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None: return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


###
### TEST
s = Solution()
nums = [1,2,3,1]
print(s.rob(nums))      # OUTPUT: 4

nums = [2,7,9,3,1]
print(s.rob(nums))      # OUTPUT: 12
