'''
To find first recurring char in a string

s1 = "ABCA"   # Return: A
s1 = "BCABA"  # Return: B
s1 = "ABC"    # Return: None
'''

class Recurring:
## Using bruteForce
## Time complexity = O(nxn)
    def findRecurringChar_bruteForce(self, s1):
        for i in range(len(s1)-1):
            firstChar = s1[i]
            for j in range(i+1, len(s1)):
                if firstChar == s1[j]:
                    return firstChar
        return None

## Using dictionary
## Time complexity = O(n)
    def findRecurringChar_optimized(self, s1):
        charDict = {}
        for i in range(len(s1)):
            if s1[i] in charDict:
                return s1[i]
            else:
                charDict[s1[i]] = 1
        return None

if __name__ == '__main__':
    rec = Recurring()
    s1 = "ABCA"   # Return: A
    print(rec.findRecurringChar_bruteForce(s1))
    s1 = "BCABA"  # Return: B
    print(rec.findRecurringChar_bruteForce(s1))
    s1 = "ABC"    # Return: None
    print(rec.findRecurringChar_bruteForce(s1))

    rec = Recurring()
    s1 = "ABCA"   # Return: A
    print(rec.findRecurringChar_optimized(s1))
    s1 = "BCABA"  # Return: B
    print(rec.findRecurringChar_optimized(s1))
    s1 = "ABC"    # Return: None
    print(rec.findRecurringChar_optimized(s1))
