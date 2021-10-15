'''
      a  c  e
   a  x        0
   b           0
   c     x     0
   d           0
   e        x  0
      0  0  0  0

   if text[i] == text[j]:
        dp[i][j] = 1 + dp[i+1][j+1]
   else:
        dp[i][i] = max(dp[i+1][j], dp[i][j+1])
'''

def lcs(str1, str2):
    dp = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
    """
    [
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]
    ]
    """
    for i in range(len(str1)-1, -1, -1):
        for j in range(len(str2)-1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]



###
### TEST
print(lcs("abcde", "ace"))    # OUTPUT: 3
print(lcs("abcde", "ae"))     # OUTPUT: 2
print(lcs("ae", "abcde"))     # OUTPUT: 2
print(lcs("abcde", "acde"))   # OUTPUT: 4
print(lcs("abcde", ""))       # OUTPUT: 0
