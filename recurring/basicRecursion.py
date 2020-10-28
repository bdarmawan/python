def fact(i):
    if i == 1:
        print (i, 1)
        return 1
    else:
        x = i * fact(i-1)
        print(i, x)
        return x


def fib(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)


# fib with memoization - optimized
def fib2(i, cache={}):
   if i in cache:
       return cache[i]
   if i == 0 or i == 1:
       return i
   result = fib(i-1) + fib(i-2)
   cache[i] = result
   return result



if __name__ == "__main__":
    print(fact(5));
    print(fib(5));
    print(fib2(5));

'''
0 1
2 2
3 6
4 24
5 120
120

5

5
'''