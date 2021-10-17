#######################################
# 1 - Brute Force Without Memoization

# m = target sum
# n = array legth
# O(n ^ m * m) time
# O(m ^ 2) space
#######################################
def bestSum(target, numbers):
    if target == 0: return []
    if target < 0: return None

    shortestAnswer = None
    for number in numbers:
        remainder = target - number
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination is not None:
            combination = remainderCombination + [number]   # Tricky !!!
            if shortestAnswer is None  or  len(combination) < len(shortestAnswer):  # Tricky !!!
                shortestAnswer = combination

    return shortestAnswer



#######################################
# 2 - With Memoization

# O(n * m ^ 2) time
# O(m ^ 2) space
#######################################
def bestSumMem(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortestAnswer = None
    for number in numbers:
        remainder = target - number
        remainderCombination = bestSumMem(remainder, numbers, memo)
        if remainderCombination != None:
            combination = remainderCombination + [number]  # Tricky !!!
            if shortestAnswer == None  or  len(combination) < len(shortestAnswer):  # Tricky !!!
                shortestAnswer = combination

    memo[target] = shortestAnswer
    return shortestAnswer


### IF you need to know the count
def bestSumMem2(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortestAnswer = None
    for number in numbers:
        remainder = target - number
        remainderCombination = bestSumMem2(remainder, numbers, memo)
        if remainderCombination != None:
            if type(remainderCombination) == list:
                combination = remainderCombination + [number]  # Tricky !!!
            else:
                combination = [remainderCombination] + [number]  # Tricky !!!

            if shortestAnswer == None  or  len(combination) < len(shortestAnswer):  # Tricky !!!
                shortestAnswer = combination

    memo[target] = shortestAnswer
    return len(shortestAnswer) if shortestAnswer != None else 0


#######################################
# 3 - With Tabulation

# O(n * m ^ 2) time
# O(m ^ 2) space
#######################################
def bestSumTab(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    combination = table[i] + [num]    # Tricky !!!
                    # we're NOT adding 'num' but appending it!!!
                    if table[i + num] is None  or  (len(table[i + num]) > len(combination)):   # Tricky !!!
                        table[i + num] = combination

    return table[targetSum]



## TEST ##
#####
# 1 #
#####
print("bestSum")
print(bestSum(8, [2, 3, 5, 10]))        # [5, 3]
#Below will time out! b/c it takes so long to process - need to be optimized with Memoize
#print(bestSum(100, [1, 2, 5, 25]))


#####
# 2 #
#####
print("bestSumMem")
print(bestSumMem(8, [2, 3, 5, 9, 10]))      # [5, 3]
print(bestSumMem(100, [1, 2, 5, 25]))       # [25, 25, 25, 25]
# print("============================")
# print(f"'>> ' {bestSum(8, [2, 3, 5])}")
# print("----------------------------")
print("")
print("bestSumMem2")
print(bestSumMem2(8, [2, 3, 5, 9, 10],{}))      # 2
print(bestSumMem2(100, [1, 2, 5, 24, 25],{}))   # 4
print(bestSumMem2(100, [1, 2, 5, 25],{}))       # 4
coins = [1, 3, 4, 5]
amount = 7
print(bestSumMem2(amount, coins,{}))            # 2 -> which is [4,3]

#####
# 3 #
#####
print("bestSumTab")
print(bestSumTab(8, [2, 3, 5, 9, 10]))     # [3, 5]
print(bestSumTab(100, [1, 2, 5, 25]))      # [25, 25, 25, 25]
