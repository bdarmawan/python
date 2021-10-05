'''
TIME:  O(amount * len(coins))
SPACE: O(amount)
'''
from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for sum in range(1, amount + 1):
        for coin in coins:
            if sum - coin >= 0:
                dp[sum] = min(dp[sum], 1 + dp[sum - coin])

    return dp[amount] if dp[amount] != amount + 1 else -1



###
### TEST
coins = [1,3,4,5]
amount = 7
print(coinChange(coins, amount))     # OUTPUT: 2

coins = [2]
amount = 3
print(coinChange(coins, amount))     # OUTPUT: -1


'''
      0 1 2 3 4 5 6 7
dp = [0,8,8,8,8,8,8,8]

for sum in range(1, 8):     #1 2 3 4 5 6 7
  for coin in coins:        #1 3 4 5
     i=1
     dp[1] = min(dp[1], 1 + dp[1-1]) = min(8, 1+0) = 1 *
     
     i=2
     dp[2] = min(dp[2], 1 + dp[2-1]) = min(8, 1+1) = 2 *

     i=3
     dp[3] = min(dp[3], 1 + dp[3-1]) = min(8, 1+2) = 3
     dp[3] = min(dp[3], 1 + dp[3-3]) = min(3, 1+0) = 1 *

     i=4
     dp[4] = min(dp[4], 1 + dp[4-1]) = min(8, 1+1) = 2
     dp[4] = min(dp[4], 1 + dp[4-3]) = min(2, 1+1) = 2
     dp[4] = min(dp[4], 1 + dp[4-4]) = min(2, 1+0) = 1 *

     i=5
     dp[5] = min(dp[5], 1 + dp[5-1]) = min(8, 1+1) = 2
     dp[5] = min(dp[5], 1 + dp[5-3]) = min(2, 1+2) = 2
     dp[5] = min(dp[5], 1 + dp[5-4]) = min(2, 1+1) = 2
     dp[5] = min(dp[5], 1 + dp[5-5]) = min(2, 1+0) = 1 *

     i=6
     dp[6] = min(dp[6], 1 + dp[6-1]) = min(8, 1+1) = 2
     dp[6] = min(dp[6], 1 + dp[6-3]) = min(2, 1+1) = 2
     dp[6] = min(dp[6], 1 + dp[6-4]) = min(2, 1+2) = 2
     dp[6] = min(dp[6], 1 + dp[6-5]) = min(2, 1+1) = 2 *

     i=7
     dp[7] = min(dp[7], 1 + dp[7-1]) = min(8, 1+2) = 3
     dp[7] = min(dp[7], 1 + dp[7-3]) = min(3, 1+1) = 2
     dp[7] = min(dp[7], 1 + dp[7-4]) = min(2, 1+1) = 2
     dp[7] = min(dp[7], 1 + dp[7-5]) = min(2, 1+2) = 2 *
     
     return dp[7] if dp[7] != 8 else -1    ---> OUTPUT: 2
'''