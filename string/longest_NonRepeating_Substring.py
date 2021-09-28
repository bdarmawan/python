def isUnique(string):
    map = {}
    for i in range(len(string)):
        if string[i] in map:
            return False
        else:
            map[string[i]] = 1
    return True

# Brute Force
# Complexity: O(N^3)
def findLongestSubstringBruteForce(string):
    maxLength = 0
    res = {}
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substring = string[i:j]
            flag = isUnique(substring)
            if flag:
                length = len(substring)
                maxLength = max(maxLength, length)
                res[substring] = maxLength
            else:
                length = 0
                maxLength = 0
            print(f"substring: {substring} ----> isUnique: {flag} : length: {length} : maxLength: {maxLength}")
    return res


# 2nd choice
# Complexity: O(N)
def findLongestSubstring(string):
    dict = {}
    start = curlen = longest = 0

    for i, c in enumerate(string):
        if c in dict and dict[c] >= start:
            start = dict[c] + 1
            curlen = i - dict[c]
        else:
            curlen += 1
            if curlen > longest:
                longest = curlen
        dict[c] = i
    return longest


# 1st choice
# Complexity: O(N)
def findLongestSubString2(string):
    i = j = longest = 0
    mySet = set()

    for j in range(len(string)):
        if string[j] not in mySet:
            mySet.add(string[j])
            j += 1
            longest = max(len(mySet), longest)
        else:
            mySet.remove(string[i])
            i += 1
    return longest



# Driver Code
if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    res = findLongestSubstringBruteForce(string)
    print(res)
    longest = max(res.values())
    for k, v in res.items():
        if v == longest:
            print(f"{k} ----> length: {len(k)}")

    print("********************************************************")
    print(findLongestSubstring(string))
    print(findLongestSubString2(string))

"""
Output: 
substring: G ----> isUnique: True : length: 1 : maxLength: 1
substring: GE ----> isUnique: True : length: 2 : maxLength: 2
substring: GEE ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEKS ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEKSF ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEKSFO ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEKSFOR ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEKSFORG ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEKSFORGE ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEKSFORGEE ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEKSFORGEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: E ----> isUnique: True : length: 1 : maxLength: 1
substring: EE ----> isUnique: False : length: 0 : maxLength: 0
substring: EEK ----> isUnique: False : length: 0 : maxLength: 0
substring: EEKS ----> isUnique: False : length: 0 : maxLength: 0
substring: EEKSF ----> isUnique: False : length: 0 : maxLength: 0
substring: EEKSFO ----> isUnique: False : length: 0 : maxLength: 0
substring: EEKSFOR ----> isUnique: False : length: 0 : maxLength: 0
substring: EEKSFORG ----> isUnique: False : length: 0 : maxLength: 0
substring: EEKSFORGE ----> isUnique: False : length: 0 : maxLength: 0
substring: EEKSFORGEE ----> isUnique: False : length: 0 : maxLength: 0
substring: EEKSFORGEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: E ----> isUnique: True : length: 1 : maxLength: 1
substring: EK ----> isUnique: True : length: 2 : maxLength: 2
substring: EKS ----> isUnique: True : length: 3 : maxLength: 3
substring: EKSF ----> isUnique: True : length: 4 : maxLength: 4
substring: EKSFO ----> isUnique: True : length: 5 : maxLength: 5
substring: EKSFOR ----> isUnique: True : length: 6 : maxLength: 6
substring: EKSFORG ----> isUnique: True : length: 7 : maxLength: 7
substring: EKSFORGE ----> isUnique: False : length: 0 : maxLength: 0
substring: EKSFORGEE ----> isUnique: False : length: 0 : maxLength: 0
substring: EKSFORGEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: K ----> isUnique: True : length: 1 : maxLength: 1
substring: KS ----> isUnique: True : length: 2 : maxLength: 2
substring: KSF ----> isUnique: True : length: 3 : maxLength: 3
substring: KSFO ----> isUnique: True : length: 4 : maxLength: 4
substring: KSFOR ----> isUnique: True : length: 5 : maxLength: 5
substring: KSFORG ----> isUnique: True : length: 6 : maxLength: 6
substring: KSFORGE ----> isUnique: True : length: 7 : maxLength: 7
substring: KSFORGEE ----> isUnique: False : length: 0 : maxLength: 0
substring: KSFORGEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: S ----> isUnique: True : length: 1 : maxLength: 1
substring: SF ----> isUnique: True : length: 2 : maxLength: 2
substring: SFO ----> isUnique: True : length: 3 : maxLength: 3
substring: SFOR ----> isUnique: True : length: 4 : maxLength: 4
substring: SFORG ----> isUnique: True : length: 5 : maxLength: 5
substring: SFORGE ----> isUnique: True : length: 6 : maxLength: 6
substring: SFORGEE ----> isUnique: False : length: 0 : maxLength: 0
substring: SFORGEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: F ----> isUnique: True : length: 1 : maxLength: 1
substring: FO ----> isUnique: True : length: 2 : maxLength: 2
substring: FOR ----> isUnique: True : length: 3 : maxLength: 3
substring: FORG ----> isUnique: True : length: 4 : maxLength: 4
substring: FORGE ----> isUnique: True : length: 5 : maxLength: 5
substring: FORGEE ----> isUnique: False : length: 0 : maxLength: 0
substring: FORGEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: O ----> isUnique: True : length: 1 : maxLength: 1
substring: OR ----> isUnique: True : length: 2 : maxLength: 2
substring: ORG ----> isUnique: True : length: 3 : maxLength: 3
substring: ORGE ----> isUnique: True : length: 4 : maxLength: 4
substring: ORGEE ----> isUnique: False : length: 0 : maxLength: 0
substring: ORGEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: R ----> isUnique: True : length: 1 : maxLength: 1
substring: RG ----> isUnique: True : length: 2 : maxLength: 2
substring: RGE ----> isUnique: True : length: 3 : maxLength: 3
substring: RGEE ----> isUnique: False : length: 0 : maxLength: 0
substring: RGEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: G ----> isUnique: True : length: 1 : maxLength: 1
substring: GE ----> isUnique: True : length: 2 : maxLength: 2
substring: GEE ----> isUnique: False : length: 0 : maxLength: 0
substring: GEEK ----> isUnique: False : length: 0 : maxLength: 0
substring: E ----> isUnique: True : length: 1 : maxLength: 1
substring: EE ----> isUnique: False : length: 0 : maxLength: 0
substring: EEK ----> isUnique: False : length: 0 : maxLength: 0
substring: E ----> isUnique: True : length: 1 : maxLength: 1
substring: EK ----> isUnique: True : length: 2 : maxLength: 2
substring: K ----> isUnique: True : length: 1 : maxLength: 2
{'G': 1, 'GE': 2, 'E': 1, 'EK': 2, 'EKS': 3, 'EKSF': 4, 'EKSFO': 5, 'EKSFOR': 6, 'EKSFORG': 7, 'K': 2, 'KS': 2, 'KSF': 3, 'KSFO': 4, 'KSFOR': 5, 'KSFORG': 6, 'KSFORGE': 7, 'S': 1, 'SF': 2, 'SFO': 3, 'SFOR': 4, 'SFORG': 5, 'SFORGE': 6, 'F': 1, 'FO': 2, 'FOR': 3, 'FORG': 4, 'FORGE': 5, 'O': 1, 'OR': 2, 'ORG': 3, 'ORGE': 4, 'R': 1, 'RG': 2, 'RGE': 3}
EKSFORG ----> length: 7
KSFORGE ----> length: 7
********************************************************
7
7
"""
