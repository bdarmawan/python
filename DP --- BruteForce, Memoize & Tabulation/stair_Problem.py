'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

###
### TEST
s = Solution()
print(s.climbStairs(4))     # OUTPUT: 5



#####################
#####################
#####################
'''
Minimum Jump to reach the top
'''
class Solution:
    def minClimbStairs(self, n: int) -> int:
        dp = [0] * n    # Give initial value > n

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n):
            dp[i] = 1 + min(dp[i - 1], dp[i - 2])

        print(dp)
        return dp[-1]

###
### TEST
s = Solution()
print("*******")
print(s.minClimbStairs(4))     # OUTPUT: [1, 1, 2, 2]
                                    # ANSWER = 2
print(s.minClimbStairs(5))     # OUTPUT: [1, 1, 2, 2, 3]
                                    # ANSWER = 3
print(s.minClimbStairs(8))     # OUTPUT: [1, 1, 2, 2, 3, 3, 4, 4]
                                    # ANSWER = 4



#####################
#####################
#####################
'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        print(dp)
        return min(dp[-2:])  # We want to find min of the last two

###
### TEST
s = Solution()
cost = [10, 15, 20]
print(s.minCostClimbingStairs(cost))        # OUTPUT: [10, 15, 30]
                                                # ANSWER = 15
cost = [1,100,1,1,1,100,1,1,100,1]      # OUTPUT: [1, 100, 2, 3, 3, 103, 4, 5, 104, 6]
print(s.minCostClimbingStairs(cost))                # ANSWER = 6
