import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 0
        for i in range(1, int(math.sqrt(num) + 1)):
            if num % i == 0:
                res += i
                print(i)
        return res == num


a = Solution()
a.checkPerfectNumber(28)
