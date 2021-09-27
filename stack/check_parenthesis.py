'''
If the stack is empty at the end of the execution
that means - all parenthesis are CHECKED
'''

def isValid(s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack  and  (i == bracket_map[stack[-1]]):
                stack.pop()
        else:
            return False
    return stack == []



str = "(({{[[[]]]}}}))"
print(f"{str} is valid: {isValid(str)}")    # False

str = "(({{[[[]]]}}))"
print(f"{str} is valid: {isValid(str)}")    # True

str = "{[()}]"
print(f"{str} is valid: {isValid(str)}")    # False

"""
(({{[[[]]]}}})) is valid: False
(({{[[[]]]}})) is valid: True
{[()}] is valid: False
"""