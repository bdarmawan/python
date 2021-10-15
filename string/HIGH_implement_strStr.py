class Solution:
    # 1st APPROACH
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        savedPosition = 0
        for i in range(len(haystack)):
            ctr = 0
            for c in needle:
                if haystack[i] == c:
                    if ctr == 0:
                        savedPosition = i
                        ctr = 1
                    else:
                        ctr += 1
                if ctr == len(needle): return savedPosition
        return -1


    # 2nd APPROACH
    def strStr2(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        for i in range(len(haystack)):
            if haystack[i:].startswith(needle) == True:
                return i
        return -1

###
### TEST
haystack = "hello"
needle = "ll"
s = Solution()
print(s.strStr(haystack, needle))      # OUTPUT: 2
print(s.strStr2(haystack, needle))      # OUTPUT: 2

haystack = "aaaaa"
needle = "bba"
print(s.strStr(haystack, needle))      # OUTPUT: 1
print(s.strStr2(haystack, needle))      # OUTPUT: 1

haystack = ""
needle = ""
print(s.strStr(haystack, needle))      # OUTPUT: None
print(s.strStr2(haystack, needle))      # OUTPUT: None

