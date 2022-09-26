from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt_maps = {}
        for idx, val in enumerate(nums):
            cnt_maps.setdefault(val, [])
            cnt_maps[val].append(idx)

        for value in cnt_maps.values():
            for i in range(1, len(value)):
                gap = value[i] - value[i - 1]
                if gap < k:
                    return True
        return False
