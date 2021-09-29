"""
OPERATOR:  + - ( )
"""
def calculate(str):
    if str is None:
        return 0

    stack = []
    currentNumber = 0
    operation = "+"  # set the default operator to be a +

    for i in range(len(str)):
        currentChar = str[i]
        if currentChar.isdigit():
            currentNumber = currentNumber * 10 + int(currentChar)

        ''' The following will do
         (
         not currentChar.isdigit() -> not a digit, e.g.:  + - * /
         not currentChar.isspace() -> not a space
         )
         OR
         it is last char of the input  ---  i == len(str) - 1   ---->   IMPORTANT
        '''
        if (not currentChar.isdigit() and (not currentChar.isspace())   or   (i == len(str)-1)):
            if operation == "+":
                stack.append(currentNumber)
            if operation == "-":
                stack.append(-currentNumber)
            if operation == "(":
                stack.append(currentNumber)
            if operation == ")":
                stack.append(stack.pop() + currentNumber)

            operation = currentChar
            currentNumber = 0


    result = 0
    for i in range(len(stack)):
        result += stack.pop()

    return result


str = "2+(3-2+5)"
print(calculate(str))   # OUTPUT: 8

str = "2+3-1"
print(calculate(str))   # OUTPUT: 4

str  = "2+ (3-0+ (1+1) +4)"
print(calculate(str))   # OUTPUT: 11
