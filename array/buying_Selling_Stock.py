import math
from typing import List
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day 
in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = math.inf

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxProfit = max(maxProfit, price - minPrice)
            print(minPrice, price, maxProfit)
        return maxProfit


###
###TEST

s = Solution()
prices = [7,1,5,3,6,4]
s.maxProfit(prices)         #OUTPUT: 5

'''
7 7 0
1 1 0
1 5 4
1 3 4
1 6 5
1 4 [5] <-------
'''


prices = [7,6,4,3,1]
s.maxProfit(prices)         #OUTPUT: 0
'''
7 7 0
6 6 0
4 4 0
3 3 0
1 1 [0] <-------
'''
