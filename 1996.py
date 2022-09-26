from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        sorted_pro = sorted(properties, key=lambda x: (-x[0], x[1]))
        res = 0
        max_defense = -1
        for elem in sorted_pro:
            if max_defense > elem[1]:
                res += 1
            max_defense = max(max_defense, elem[1])
        return res