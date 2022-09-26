from typing import List

import numpy as np


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        assert grid
        h = len(grid)
        w = len(grid[0])

        visited = np.zeros((h, w), dtype=bool)
        target = grid[row][col]

        index_set = set()

        queue = [(row, col)]
        while queue:
            x, y = queue.pop()
            if not self.out_of_edge(x, y, h, w) and not visited[x][y]:
                value = grid[x][y]
                visited[x][y] = True
                if value == target:
                    index_set.add((x, y))
                    neighbors = self.get_neighbor(x, y)
                    queue.extend(neighbors)
        for x, y in index_set:
            neighbors = self.get_neighbor(x, y)
            cnt = 0
            for neighbor in neighbors:
                if neighbor in index_set:
                    cnt += 1
            if cnt < 4:
                grid[x][y] = color
        return grid

    def out_of_edge(self, x, y, h, w):
        horizontal_check = 0 <= x < h
        vertical_check = 0 <= y < w
        return not (horizontal_check and vertical_check)

    def get_neighbor(self, x, y):
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


a = Solution()
res = a.colorBorder([[1, 2, 2], [2, 3, 2]]
                    , 0
                    , 1
                    , 3)
print(res)
