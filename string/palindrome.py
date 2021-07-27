def palindrome(string) -> bool:
	if (type(string) != str):
		return False
	if (len(string) == 0):
		return False

	mid = len(string) // 2
	if len(string) % 2 == 0:      # if len(string) EVEN
		leftToRight = string[:mid]
		rightToLeft = string[len(string):mid-1:-1]
		print("==> ", leftToRight, rightToLeft, leftToRight == rightToLeft)
	else:                      # if len(string) ODD
		leftToRight = string[:mid]
		rightToLeft = string[len(string):mid:-1]
		print("==> ", leftToRight, rightToLeft, leftToRight == rightToLeft)
	return leftToRight == rightToLeft



string = "ABCBA"
print(f"Is {string} palindrome? {palindrome(string)}")

string = "ABBA"
print(f"Is {string} palindrome? {palindrome(string)}")

string = "ABCDBA"
print(f"Is {string} palindrome? {palindrome(string)}")

string = ""
print(f"Is {string} palindrome? {palindrome(string)}")

string = 1221
print(f"Is {string} palindrome? {palindrome(string)}")

string = "1221"
print(f"Is {string} palindrome? {palindrome(string)}")

string = "AB C BA"
print(f"Is {string} palindrome? {palindrome(string)}")
