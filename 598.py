class Solution:
    def maxCount(self, m, n, ops):
        min_m = 50000
        min_n = 50000
        for i in ops:
            min_m = min(i[0], min_m)
            min_n = min(i[1], min_n)
        return min_m * min_n
