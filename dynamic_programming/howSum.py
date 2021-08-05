def howSum(target, numbers):
	if target == 0:
		return []
	if target < 0:
		return None

	for number in numbers:
		remainder = target - number
		combination = howSum(remainder, numbers)
		if combination != None:
			combination.append(number)
			return combination

	return None



def howSumMem(target, numbers, memo={}):
	if target in memo:
		return memo[target]
	if target == 0:
		return []
	if target < 0:
		return None

	for number in numbers:
		remainder = target - number
		combination = howSum(remainder, numbers)
		if combination != None:
			memo[target] = number
			combination.append(number)
			return combination

	return None



print(howSum(7, [2,3]))
print(howSum(8, [2,3,5 ]))

print(howSumMem(7, [2,3], {}))
print(howSumMem(8, [2,3,5], {}))
