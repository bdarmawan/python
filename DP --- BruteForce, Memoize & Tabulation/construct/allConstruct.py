'''
The function should return a 2D array containing "all of the ways"
that the "target" can be constructed by concatenating elements of
the "wordBank" array.
'''

#######################################
# 1 - Brute Force Without Memoization

# m = target
# n = wordBank length
# O(n ^ m * m) time
# O(m ^ 2) space
#######################################
def allConstruct_WithoutMemoization(target, wordBank):
	if target == "": return [[]]

	result = []

	for word in wordBank:
		if target.startswith(word) == True:
			remainder = target[len(word):]
			remainderWays = allConstruct_WithoutMemoization(remainder, wordBank)
			for remainderWay in remainderWays:       # this is very tricky
				targetWays = remainderWay + [word]   # we want to iterate for every subarray
				result.append(targetWays)            # and append [word]

	return result

#########################
# 2 - With Memoization

# O(n ^ m) time
# O(m) space
#########################
def allConstruct(target, wordBank, memo={}):
	if target in memo: return memo[target]
	if target == "": return [[]]

	result = []

	for word in wordBank:
		if target.startswith(word) == True:
			remainder = target[len(word):]
			remainderWays = allConstruct(remainder, wordBank, memo)
			for remainderWay in remainderWays:
				targetWays = remainderWay + [word]
				result.append(targetWays)
				memo[target] = result

	return result


'''
HAS ISSUE !!!!!!!!!!!!!!!!!!!!!!!!
'''
#########################
# 3 - With Tabulation

# O(n ^ m) time
# O(n ^ m) space
#########################
def allConstructTab(target, wordBank):
	table = [[]] * (len(target) + 1)
	table[0] = [[]]      # for empty string there's 1 combination available
	print(table)

	for i in range(len(target)):
		for word in wordBank:
			if target[i:i + len(word)] == word:
				for subArray in table[i]:
					newCombination = subArray + [word]      # HAS ISSUE HERE !!!
					table[i + len(word)] = newCombination
	return table(len(target))







## TEST ##
#####
# 1 #
#####
print(allConstruct_WithoutMemoization('purple', ['purp','p','ur','le']))
'''
OUTPUT:
[
	['le', 'purp']
	['le', 'p', 'ur', 'p']
]
'''
print(allConstruct_WithoutMemoization('purple', ['purp','p','ur','le','purpl']))
'''
OUTPUT:
[
	['le', 'purp']
	['le', 'p', 'ur', 'p']
]
'''
print(allConstruct_WithoutMemoization('abcdef', ['ab','abc','cd','def','abcd','ef','c']))
'''
OUTPUT:
[
	['ef', 'cd', 'ab']
	['def', 'c', 'ab']
	['def', 'abc']
	['ef', 'abcd']
]
'''
print(allConstruct_WithoutMemoization('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
'''
OUTPUT:
[]
'''
print(allConstruct_WithoutMemoization('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
'''
OUTPUT:
[
	['ot', 'p', 'ent', 'ot', 'p', 'a', 'enter']
	['t', 'o', 'p', 'ent', 'ot', 'p', 'a', 'enter']
	['ot', 'p', 'ent', 't', 'o', 'p', 'a', 'enter']
	['t', 'o', 'p', 'ent', 't', 'o', 'p', 'a', 'enter']
]
'''
# Below will time out -> need to use memoize
"""
print(allConstruct_WithoutMemoization('eeeeeeeeeeeeeeeeeeeeeeeeef', [
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
print(allConstruct('purple', ['purp','p','ur','le'], {}))
'''
OUTPUT:
[
	['le', 'purp']
	['le', 'p', 'ur', 'p']
]
'''
print(allConstruct('purple', ['purp','p','ur','le','purpl'], {}))
'''
OUTPUT:
[
	['le', 'purp']
	['le', 'p', 'ur', 'p']
]
'''
print(allConstruct('abcdef', ['ab','abc','cd','def','abcd','ef','c'], {}))
'''
OUTPUT:
[
	['ef', 'cd', 'ab']
	['def', 'c', 'ab']
	['def', 'abc']
	['ef', 'abcd']
]
'''
print(allConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar'], {}))
'''
OUTPUT:
[]
'''
print(allConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t'], {}))
'''
OUTPUT:
[
	['ot', 'p', 'ent', 'ot', 'p', 'a', 'enter']
	['t', 'o', 'p', 'ent', 'ot', 'p', 'a', 'enter']
	['ot', 'p', 'ent', 't', 'o', 'p', 'a', 'enter']
	['t', 'o', 'p', 'ent', 't', 'o', 'p', 'a', 'enter']
]
'''
# Below is still a bit slow
"""
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeef', [
	'e',
	'ee',
	'eee',
	'eeee',
	'eeeee'
], {}))
"""
'''
OUTPUT:
[]
'''
print("")



#####
# 3 #
#####
print(allConstructTab('purple', ['purp','p','le']))
'''
OUTPUT:
[
	['le', 'purp']
	['le', 'p', 'ur', 'p']
]
'''