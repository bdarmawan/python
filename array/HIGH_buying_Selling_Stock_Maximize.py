'''
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

def stockmax(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += (prices[i] - prices[i-1])
    return profit

###
### TEST
prices = [7,1,5,3,6,4]
print(stockmax(prices))     #OUTPUT : 7
                            # (-1 + 5) + (-3 + 6)

prices = [5, 3, 2]
print(stockmax(prices))     #OUTPUT : 0

prices = [1, 2, 100]
print(stockmax(prices))     #OUTPUT : 99
                            # (-1 + 2) + (-2 + 100)
prices =[1, 3, 1, 2]
print(stockmax(prices))     #OUTPUT : 3
                            # (-1 + 3) + (-1 + 2)

prices = [10, 22, 5, 75, 65, 80]
print(stockmax(prices))     #OUTPUT : 97
                            # (-10 + 22) + (-5 + 75) + (-65 + 80)

