#######################################
# 1 - Brute Force Without Memoization

# m = target sum
# n = array legth
# O(n ^ m * m) time
# O(m) space
#######################################
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


#######################################
# 2 - With Memoization

# O(n * m * m) time
# O(m ^ 2) space
#######################################
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


#######################################
# 3 - With Tabulation

# O(n * m * m) time
# O(m ^ 2) space
#######################################
def howSumTab(targetSum, numbers):
	table = [None] * (targetSum + 1)  # Initialize table
	table[0] = []					  # Seed

	for i in range(targetSum):
		if table[i] is not None:
			for num in numbers:
				if i + num <= targetSum:
					table[i + num] = table[i] + [num]  # Tricky !!!
                                       # we're NOT adding 'num' but appending it!!!
	return table[targetSum]




## TEST ##
#####
# 1 #
#####
print(howSum(7, [2,3])) 	# [3, 2, 2]
print(howSum(8, [2,3,5]))	# [2, 2, 2, 2]
print(howSum(8, [3,7,9]))	# None
# print("")

#####
# 2 #
#####
print(howSumMem(7, [2,3], {}))		# [3, 2, 2]
print(howSumMem(8, [2,3,5], {}))	# [2, 2, 2, 2]
print(howSumMem(8, [3,7,9]))	# None
print("")

#####
# 3 #
#####
print(howSumTab(7, [2,3]))		# [3, 2, 2]
print(howSumTab(8, [2,3,5]))	# [2, 2, 2, 2]
print(howSumTab(8, [3,7,9]))	# None
