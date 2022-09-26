class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        res = 28 * weeks + weeks * (weeks - 1) * 7 / 2

        base = weeks
        for i in range(days):
            res += base + i + 1
        print(res)
        return int(res)


a = Solution()
a.totalMoney(10)
