'''
Reverse a string without affecting special characters

Given a string, that contains a special character together with alphabets
(‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that
special characters are not affected.

Algo:  Use left, right pointer
1) Let input string be 'str[]' and length of string be 'n'
2) l = 0, r = n-1
3) While l is smaller than r, do following
    a) If str[l] is not an alphabetic character, do l++
    b) Else If str[r] is not an alphabetic character, do r--
    c) Else swap str[l] and str[r]
'''

def swap(str):
	myString = list(str)
	left, right = 0, len(myString)-1
	while left < right:
		if not(myString[left].isalpha()):   left += 1
		elif not(myString[right].isalpha()):  right -= 1
		else:
			tmp = myString[left]
			myString[left] = myString[right]
			myString[right] = tmp
			left += 1
			right -= 1

	return ''.join(myString)



###
###TEST
str = "Ab,c,de!$"
print(f'Original : {str}')
print(f'Swapped  : {swap(str)}')
'''
Original : Ab,c,de!$
Swapped  : ed,c,bA!$
'''


str = "Hello"
print(f'Original : {str}')
print(f'Swapped  : {swap(str)}')
'''
Original : Hello
Swapped  : olleH
'''

str = "a,b$c"
print(f'Original : {str}')
print(f'Swapped  : {swap(str)}')
'''
Original : a,b$c
Swapped  : c,b$a
'''