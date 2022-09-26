from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if not score:
            return []

        elems = [[v, i] for i, v in enumerate(score)]
        elems = sorted(elems, key=lambda x: x[0], reverse=True)
        special = True

        for i in range(len(elems)):
            if special:
                if i == 0:
                    elems[i][0] = 'Gold Medal'
                elif i == 1:
                    elems[i][0] = 'Silver Medal'
                elif i == 2:
                    elems[i][0] = 'Bronze Medal'
                    special = False
            else:
                elems[i][0] = str(i + 1)
        elems = sorted(elems, key=lambda x: x[1])
        res = [elem[0] for elem in elems]
        return res
