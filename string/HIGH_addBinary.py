'''
case I: -----*
             |
             v
carry =      1 1 1 1 1 0
a =            1 1 1 0 1
b =            1 1 0 1 1
------------------------ +
             1 1 1 0 0 0


case II: ----*
             |
             v
carry =      1 1 1 1 1 0
a =            1 1 1 0 1
b =            0 1 0 1 1
------------------------ +
             1 0 1 0 0 0


case III:
carry =        0 1 1 1 0
a =            1 0 1 0 1
b =            0 0 0 1 1
------------------------ +
               1 1 0 0 0
'''


def addBinary(a: str, b:str) -> str:
    carry = 0
    result = ""

    a, b = list(a), list(b)   # easier to conver it to a list
                              # so you can iterate

    while a or b or carry == 1:   # carry == 1 is to handle case I and II
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        result += str(carry % 2)
        carry = carry // 2

    return result[::-1]   # we need to reverse, b/c we did pop() operation earlier


###
### TEST
a = "11101"
b = "11011"
print(addBinary(a, b))   # OUTPUT: 111000

a = "11101"
b = " 1011"
print(addBinary(a, b))   # OUTPUT: "101000"

a = "10101"
b = "   11"
print(addBinary(a, b))   # OUTPUT: "11000"

