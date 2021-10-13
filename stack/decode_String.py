class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":                 # create stack until it finds ]
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":     # loop to construct what's after [
                    substr = stack.pop() + substr
                stack.pop()                 # this is to popup [

                k = ""
                while stack and stack[-1].isdigit():    # loop to construct number(s)
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)


###
###TEST
s = Solution()

string = "3[a]2[bc]"
print(s.decodeString(string))       #OUTPUT: aaabcbc
string = "3[a2[c]]"
print(s.decodeString(string))       #OUTPUT: accaccacc
string = "2[abc]3[cd]ef"
print(s.decodeString(string))       #OUTPUT: abcabccdcdcdef
string = "abc3[cd]xyz"
print(s.decodeString(string))       #OUTPUT: abccdcdcdxyz
