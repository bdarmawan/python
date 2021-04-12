def calculate(str):
    if str is None:
        return 0

    stack = []
    currentNumber = 0
    result = 0
    sign = 1

    for i in range(len(str)):
        currentChar = str[i]
        if currentChar.isdigit():
            currentNumber = currentNumber * 10 + int(currentChar)
            result += currentNumber * sign

        if (not currentChar.isdigit() and (not currentChar.isspace()) or (i == len(str)-1)):
        # it is important for the --- or (i == len(str) -1)
        # because we want the following lines to be executed at the end of str
        # even the last char is not an operator nor space
            if currentChar == "+":
                sign = 1
            if currentChar == "-":
                sign = -1
            if currentChar == "(":
                stack.append(result)
                result = 0  # we need to reset result to 0 since we have put in the latest result in stack
                sign = 1
            if currentChar == ")":
                result += stack.pop() + sign * currentNumber
        currentNumber = 0


    return result


#str = "2+(3-2+5)"
#str = "2+3-1"
str  = "2+ (3-0+ (1+1) +4)"
print(calculate(str))