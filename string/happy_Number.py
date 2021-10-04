class Solution:
    def isHappy(self, n: int) -> bool:
        trial = 0
        while n != 1 and trial < 1000:
            number = str(n)
            res = 0
            for num in number:
                res += int(num) ** 2
            n = res
            trial += 1
        if trial == 1000:
            return False
        else:
            return True


###
###TEST
s = Solution()
print(f"Is 19 happy number? {s.isHappy(19)}")    # True
print(f"Is  2 happy number? {s.isHappy(2)}")     # False
