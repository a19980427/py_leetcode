from itertools import combinations


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        for i in combinations(range(n), 4):
            print(i)


a = Solution()
a.kInversePairs(5, 3)
