class Solution:
    def convertToBase7(self, num: int) -> str:
        res = []
        rev = num < 0

        num = abs(num)
        while num // 7 > 0:
            res.append(str(num % 7))
            num = num // 7
        res.append(str(num))

        if rev:
            res.append('-')

        return ''.join(reversed(res))
