#######################################
# 1 - Brute Force Without Memoization

# n = nth fibonacci
# O(2 ^ n) time
# O(n) space
#######################################
def fib(num):
   if num == 1 or num == 2:
       return 1

   return fib(num - 1) + fib(num - 2)


#######################################
# 2 - With Memoization

# O(n) time
# O(n) space
#######################################
def fibMemo(num, memo={}):
    if num in memo: return memo[num]
    if num == 1 or num == 2: return 1

    result = fibMemo(num - 1, memo) + fibMemo(num - 2, memo)
    memo[num] = result
    return result


#######################################
# 3 - With Tabulation

# O(n) time
# O(n) space
#######################################
def fibTab(num):
    table = [0] * (num + 1)
    table[1] = 1

    for i in range(num):
        if i + 1 <= num: table[i + 1] += table[i]
        if i + 2 <= num: table[i + 2] += table[i]
    return table[num]





## TEST ##
#####
# 1 #
#####
#i:    0  1  2  3  4  5  6
#fib:  1  1  1  2  3  5  8
print(fib(4))   # 3
print(fib(5))   # 5
print(fib(6))   # 8
print("")

#####
# 2 #
#####
print(fibMemo(4, {}))   # 3
print(fibMemo(5, {}))   # 5
print(fibMemo(6, {}))   # 8
print("")

#####
# 3 #
#####
print(fibTab(4))   # 3
print(fibTab(5))   # 5
print(fibTab(6))   # 8
