from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)

        if length != m * n:
            return []

        return [[original[j * n + i] for i in range(n)] for j in range(m)]


a = Solution()
a.construct2DArray([1, 1, 1, 1], 4, 1)

# x 1.5x 3x

# 1 3 6
