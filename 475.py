from bisect import bisect
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        res = 0
        for house in houses:
            # 寻找house右侧的第一个供暖器
            j = bisect(heaters, house)
            i = j - 1
            right_distance = heaters[j] - house if j < len(heaters) else float('inf')
            left_distance = house - heaters[i] if i >= 0 else float('inf')
            distance = min(right_distance, left_distance)
            res = max(res, distance)
        return res


a = Solution()
res = a.findRadius([1, 2, 3, 4]
                   , [1, 4])
print(res)
