from typing import List

import numpy as np


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid = np.array(grid)

        col_max = np.max(grid, axis=0)
        row_max = np.max(grid, axis=1)

        res = 0

        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                gap = min(row_max[i], col_max[j]) - grid[i][j]
                res += gap

        return int(res)


a = Solution()
a.maxIncreaseKeepingSkyline(grid=[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
