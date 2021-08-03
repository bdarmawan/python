def howSum(target, numbers):
	if target == 0:
		return []
	if target < 0:
		return None

	for number in numbers:
		remainder = target - number
		if howSum(remainder, numbers) != None:
			res.append(number)
			return res

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
		if howSumMem(remainder, numbers, memo) != None:
			memo[target] = [number]
			res.append(number)
			return res

	return None



res = []
print(howSum(7, [2,3]))
res = []
print(howSum(8, [2,3,5 ]))

res = []
print(howSumMem(7, [2,3], {}))
res = []
print(howSumMem(8, [2,3,5], {}))
