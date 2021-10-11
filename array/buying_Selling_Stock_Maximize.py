'''
Each day, you can either buy one share of WOT, sell any number of shares
or not make any transaction at all.
What is the maximum profit you can obtain with an optimum trading strategy?
'''

def stockmax(prices):
    res = []
    for i in range(len(prices)):
        profit = 0
        buyPrice = -prices[i]
        for j in range(i+1, len(prices)):
            tmpProfit = buyPrice + prices[j]
            profit = max(profit, tmpProfit)
        res.append(profit)
    print(res)
    return sum(res)


###
### TEST

prices = [5, 3, 2]
print(stockmax(prices))     #OUTPUT : 0

prices = [1, 2, 100]
print(stockmax(prices))     #OUTPUT : 197
                            # (-1 + 2) + (-1 + 100)

prices =[1, 3, 1, 2]
print(stockmax(prices))     #OUTPUT : 3
                            # (-1 + 3) + (-1 + 2)

prices = [10, 22, 5, 75, 65, 80]
print(stockmax(prices))     #OUTPUT : 3
                            # (-1 + 3) + (-1 + 2)
