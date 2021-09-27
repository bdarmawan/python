#######################################
# 1 - Brute Force Without Memoization

# m = target
# n = wordBank length
# O(n ^ m * m) time
# O(m ^ 2) space
#######################################
def countConstruct_WithoutMemoize(target, wordBank):
    if target == "": return 1

    totalCount = 0

    for word in wordBank:
        if target.startswith(word) == True:
            remainder = target[len(word):]
            numWays = countConstruct_WithoutMemoize(remainder, wordBank)
            totalCount += numWays

    return totalCount


#########################
# 2 - With Memoization

# O(n * m ^ 2) time
# O(m ^ 2) space
#########################
def countConstruct(target, wordBank, memo={}):
    if target in memo: return memo[target]
    if target == "": return 1

    totalCount = 0

    for word in wordBank:
        if target.startswith(word) == True:
            remainder = target[len(word):]
            numWays = countConstruct(remainder, wordBank, memo)
            totalCount += numWays
            memo[target] = totalCount

    return totalCount


#########################
# 3 - With Tabulation

# O(n * m ^ 2) time
# O(m) space
#########################
def countConstructTab(target, wordBank):
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(target)):
        for word in wordBank:
            if target[i:i + len(word)] == word:
                table[i + len(word)] += table[i]

    return table[len(target)]


## TEST ##
#####
# 1 #
#####
print(countConstruct_WithoutMemoize('purple', ['purp','p','ur','le','purpl']))
print(countConstruct_WithoutMemoize('abcdef', ['ab','abc','cd','def','abcd']))
print(countConstruct_WithoutMemoize('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
print(countConstruct_WithoutMemoize('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
# Below will time out -> need to use memoize
"""
print(countConstruct_WithoutMemoize('eeeeeeeeeeeeeeeeeeeeeeeeef', [
	'e',
	'ee',
	'eee',
	'eeee',
	'eeeee'
]))
"""
print('')

#####
# 2 #
#####
print(countConstruct('purple', ['purp','p','ur','le','purpl']))     # 2
print(countConstruct('abcdef', ['ab','abc','cd','def','abcd']))     # 1
print(countConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))    # 0
print(countConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))  # 4
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeef', [    # 0
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
print(countConstructTab('purple', ['purp','p','ur','le','purpl']))  # 2
print(countConstructTab('abcdef', ['ab','abc','cd','def','abcd']))  # 1
print(countConstructTab('skateboard', ['bo','rd','ate','t','ska','sk','boar']))     # 0
print(countConstructTab('enterapotentpot', ['a','p','ent','enter','ot','o','t']))   # 4
print(countConstructTab('eeeeeeeeeeeeeeeeeeeeeeeeef', [                             # 0
	'e',
	'ee',
	'eee',
	'eeee',
	'eeeee'
]))
print("")
