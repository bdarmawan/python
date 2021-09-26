#######################################
# 1 - Brute Force Without Memoization

# m = target sum
# n = array legth
# O(n ^ m) time
# O(m) space
#######################################
def canSum_WithoutMemoization(target, numbers):
	if target == 0:
		return True
	if target < 0:
		return False

	for number in numbers:
		remainder = target - number
		if canSum_WithoutMemoization(remainder, numbers) == True:
			return True

	return False



#########################
# 2 - With Memoization

# O(n * m) time
# O(m) space
#########################
def canSumMemoization(target, numbers, memo):
	if target in memo:
		return memo[target]
	if target == 0:
		return True
	if target < 0:
		return False

	for number in numbers:
		remainder = target - number
		if canSumMemoization(remainder, numbers, memo) == True:
			memo[target] = True
			return True

	memo[target] = False
	return False



def canSum(target, numbers):
	return canSumMemoization(target, numbers, {})



#########################
# 3 - With Tabulation

# O(m * n) time
# O(m) space
#########################
def canSumTab(targetSum, numbers):
	table = [False] * (targetSum + 1)   # initialize table with False
	table[0] = True						# except the 1st element

	for i in range(targetSum):
		if (table[i] == True):			# only proceed if the current element in the table is True
			for num in numbers:
				if i + num <= targetSum:  # this is for safe guard -> not exceeding the array
					table[i + num] = True

	return table[targetSum]





## TEST ##
#####
# 1 #
#####

print(canSum_WithoutMemoization(7, [2, 3]))	# True
print(canSum_WithoutMemoization(7, [5, 3, 4, 7]))	# True
print(canSum_WithoutMemoization(7, [2, 4]))	# False
print("")


#####
# 2 #
#####
print(canSum(7, [2, 3]))	# True
print(canSum(7, [5, 3, 4, 7]))	# True
print(canSum(7, [2, 4]))	# False
print("")
print(canSumMemoization(7, [2, 3], {}))	# True
print(canSumMemoization(7, [5, 3, 4, 7], {}))	# True
print(canSumMemoization(7, [2, 4], {}))	# False
print("")

#####
# 3 #
#####
print(canSumTab(7, [2, 3]))		# True
print(canSumTab(7, [5, 3, 4, 7]))	# True
print(canSumTab(7, [2, 4]))	# False