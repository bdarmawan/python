from typing import List    # this is needed for line #3 below (List[])

###
### 1st Option
def plusOne(digits: List[int]) -> List[int]:
    digits = digits[::-1]
    carry = 1
    i = 0

    while carry and i < len(digits):
        if digits[i] == 9:
            digits[i] = 0
            carry = 1
        else:
            digits[i] += 1
            carry = 0
        i += 1

    if carry:
        digits.append(1)

    return digits[::-1]


###
### 2nd Option
def plusOne_v2(digits: List[int]) -> List[int]:
    digits = digits[::-1]     # reverse the order
    carry, i = 1, 0

    while carry:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0    # leave carry as 1
            else:
                digits[i] += 1   # the addition is not becoming 10 so just add the digit
                carry = 0        # since it is < 10, set carry = 0
        else:
            digits.append(1)     # this is to handle overflow
            carry = 0            # since it is overflow, set carry = 0
        i += 1

    return digits[::-1]          # reverse it back since we reverse at the beginning at line #2


###
### TEST
digits = [9,0,0]
print(plusOne(digits))     # OUTPUT: [9, 0, 1]
print(plusOne_v2(digits))     # OUTPUT: [9, 0, 1]

digits = [9,9,9]
print(plusOne(digits))     # OUTPUT: [1, 0, 0, 0]
print(plusOne_v2(digits))     # OUTPUT: [1, 0, 0, 0]

digits = [0]
print(plusOne(digits))     # OUTPUT: [1]
print(plusOne_v2(digits))     # OUTPUT: [1]

digits = [9]
print(plusOne(digits))     # OUTPUT: [1, 0]
print(plusOne_v2(digits))     # OUTPUT: [1, 0]
