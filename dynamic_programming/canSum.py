def canSumHelper(target, numbers, memo={}):
	if target in memo:
		return memo[target]
	if target == 0:
		return True
	if target < 0:
		return False

	for number in numbers:
		remainder = target - number
		if canSumHelper(remainder, numbers, memo) == True:
			memo[target] = True
			return True

	memo[target] = False
	return False



def canSum(target, numbers):
	return canSumHelper(target, numbers, {})


print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
