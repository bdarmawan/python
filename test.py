import math
import sys

### Question 1:
### Fibonnaci
#str = sys.stdin.readline()
str = "1 2 3"
strs = str.split()
f1 = int(strs[0])
f2 = int(strs[1])
result = f1 + f2

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(strs[2])
print(f"Result: {fib(n)}")
print(f"Result fib(0): {fib(0)}")
print(f"Result fib(1): {fib(1)}")
print(f"Result fib(2): {fib(2)}")
print(f"Result fib(3): {fib(3)}")
print(f"Result fib(4): {fib(4)}")
print(f"Result fib(5): {fib(5)}")


### Question 2:
# Progress Bar
"""
input: XX--
output: 50

input: 0.....
output: 16
"""
#input = sys.stdin.readline()
input = "XX__"
n = len(input)
char1 = input[0]
print(f"Length: {n}")
lastPosition = input.rfind(char1,0,n) + 1
print(f"Last Position of {char1}: {lastPosition}")
output = math.floor((lastPosition)/n * 100)
print(f"Progress: {output}")


### Question 3:
print("\n\n")
string = 'apple'
sorted_chars = sorted(string, reverse=True)
sorted_string = ''.join(sorted_chars)
print(f"Result: {sorted_string}")

"""
pplea
"""


### Question 4:
print("How many lines?")
numOfLine=sys.stdin.readline()
print(numOfLine)
line = []
for i in (range(int(numOfLine))):
    line.append(sys.stdin.readline()[::-1].strip())

for i in (range(len(line))):
   strs = line[i].split()
   print(" ".join(strs))
#   for i in (range(len(strs))):
#       print(strs[i], end=" ")
#   print(" ")


"""
3
3

remnoteo is awesome
test is difficult
oh boy

emosewa si oetonmer  
tluciffid si tset  
yob ho  

"""


