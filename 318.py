from typing import List

import numpy as np


class Solution:
    def maxProduct(self, words: List[str]):
        map = {}
        word_cnt = len(words)
        res = 0
        for i in range(word_cnt):
            for j in range(i + 1, word_cnt):
                for index in (i, j):
                    if map.get(index, True):
                        map[index] = set(words[index])
                set_i = map.get(i)
                set_j = map.get(j)
                if not set_i & set_j:
                    res = max(res, len(words[i] * len(words[j])))
        return res

