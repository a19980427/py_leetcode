import collections
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = len(hand)
        group_nums = cnt // groupSize

        if cnt % groupSize != 0:
            return False

        cnt_map = collections.Counter(hand)
        val_set = sorted(set(cnt_map.keys()))

        for i in range(group_nums):
            min_val = self.find_min(cnt_map, val_set)
            for val in range(min_val + 1, min_val + groupSize):
                if cnt_map[val] > 0:
                    self.get_val(cnt_map, val)
                else:
                    return False
        return True

    def find_min(self, cnt_map, val_set):
        for val in val_set:
            if cnt_map[val] > 0:
                return self.get_val(cnt_map, val)
        return -1

    def get_val(self, cnt_map, val):
        cnt_map[val] -= 1
        return val


a = Solution()
a.isNStraightHand([1, 2, 3, 4, 5, 6], 2)
