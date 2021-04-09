def isValid(s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []



str = "(({{[[[]]]}}}))"
print(f"{str} is valid: {isValid(str)}")

str = "{[()}]"
print(f"{str} is valid: {isValid(str)}")

"""
(({{[[[]]]}}})) is valid: False
{[()}] is valid: False
"""