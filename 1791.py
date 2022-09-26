from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        length = len(edges)
        map_cnt = {}
        for edge in edges:
            v1, v2 = edge
            map_cnt.setdefault(v1, 0)
            map_cnt.setdefault(v2, 0)
            map_cnt[v1] += 1
            map_cnt[v2] += 1
        for k, v in map_cnt.items():
            if v == length - 1:
                return k
