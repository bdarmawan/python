def bestSum(target, numbers):
    if target == 0:
        return []
    if target < 0:
        return None

    shortestAnswer = None
    for number in numbers:
        remainder = target - number
        combination = bestSum(remainder, numbers)
        if combination is not None:
            combination.append(number)
            if shortestAnswer is None or len(combination) < len(shortestAnswer):
                shortestAnswer = combination

    return shortestAnswer




def bestSumMem(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortestAnswer = None
    for number in numbers:
        remainder = target - number
        combination = bestSumMem(remainder, numbers, memo)
        if combination != None:
            combination.append(number)
            if shortestAnswer == None or len(combination) < len(shortestAnswer):
                shortestAnswer = combination

    memo[target] = shortestAnswer
    return shortestAnswer




print(bestSum(8, [2, 3, 5, 10]))
print(bestSumMem(8, [2, 3, 5, 9, 10]))
# print("============================")
# print(f"'>> ' {bestSum(8, [2, 3, 5])}")
# print("----------------------------")
