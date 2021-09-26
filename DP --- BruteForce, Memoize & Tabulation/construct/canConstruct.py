#######################################
# 1 - Brute Force Without Memoization

# m = target
# n = wordBank length
# O(n ^ m * m) time
# O(m ^ 2) space
#######################################
def canConstruct_WithoutMemoization(target, wordBank):
	if target == "": return True

	for word in wordBank:
		if target.startswith(word) == True:    # important!  the key!
			remainder = target[len(word):]
			if canConstruct_WithoutMemoization(remainder, wordBank) == True:
				return True
	return False



#########################
# 2 - With Memoization

# O(n * m ^ 2) time
# O(m ^ 2) space
#########################
def canConstruct(target, wordBank, memo={}):
	if target in memo: return memo[target]
	if target == "": return True

	for word in wordBank:
		if target.startswith(word) == True:
			remainder = target[len(word):]
			if canConstruct(remainder, wordBank, memo) == True:
				memo[target] = True
				return True
	return False


#########################
# 3 - With Tabulation

# O(n * m ^ 2) time
# O(m) space
#########################
def canConstructTab(target, wordBank):
	table = [False] * (len(target) + 1)
	table[0] = True

	for i in range(len(target)):
		if table[i] == True:
			for word in wordBank:
				if target[i:i + len(word)] == word:
					table[i + len(word)] = True
	return table[len(target)]


## TEST ##
#####
# 1 #
#####
print(canConstruct_WithoutMemoization('abcdef', ['ab','abc','cd','def','abcd']))
print(canConstruct_WithoutMemoization('skateboard', ['bp','rd','ate','t','ska','sk','boar']))
print(canConstruct_WithoutMemoization('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
# Below will time out -> need to use memoize
"""
print(canConstruct_WithoutMemoization('eeeeeeeeeeeeeeeeeeeeeeeeef', [
	'e',
	'ee',
	'eee',
	'eeee',
	'eeeee'
]))
"""
print("")


#####
# 2 #
#####
print(canConstruct('abcdef', ['ab','abc','cd','def','abcd']))
print(canConstruct('skateboard', ['bp','rd','ate','t','ska','sk','boar']))
print(canConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
# Below is still a bit slow
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeef', [
	'e',
	'ee',
	'eee',
	'eeee',
	'eeeee'
]))
print("")


#####
# 3 #
#####
print(canConstructTab('abcdef', ['ab','abc','cd','def','abcd']))
print(canConstructTab('skateboard', ['bp','rd','ate','t','ska','sk','boar']))
print(canConstructTab('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
print(canConstructTab('eeeeeeeeeeeeeeeeeeeeeeeeef', [
	'e',
	'ee',
	'eee',
	'eeee',
	'eeeee'
]))
print("")
