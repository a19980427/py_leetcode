from typing import List

import numpy as np


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.grid = grid

        self.size = (len(grid), len(grid[0]))

        res = 0
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                visited = np.zeros(shape=self.size)
                score = self.search((i, j), visited)
                res = max(res, score)
        return res

    def search(self, loc, visited):
        score = 0
        direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dire in direct:
            tmp_loc = [x1 + x2 for x1, x2 in zip(dire, loc)]
            # 可以访问
            if self.check_index(tmp_loc) and self.grid[tmp_loc[0]][tmp_loc[1]] != 0 and visited[tmp_loc[0]][
                tmp_loc[1]] == 0:
                visited[tmp_loc[0]][tmp_loc[1]] = 1
                score = max(score, self.grid[tmp_loc[0]][tmp_loc[1]] + self.search(tmp_loc, visited))
        return score

    # def check_index(self, x, y):
    #     # 上
    #     if x - 1 < 0:
    #         return False
    #     # 下
    #     if x + 1 >= self.size[0]:
    #         return False
    #     # 左
    #     if y - 1 < 0:
    #         return False
    #     # 右
    #     if y + 1 >= self.size[1]:
    #         return False
    #     return True

    def check_index(self, loc):
        x, y = loc
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]


a = Solution()
a.getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]])
