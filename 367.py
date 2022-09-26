class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        res = i
        while res <= num:
            if res == num:
                return True
            else:
                i += 1
                res = i * i
        return False
