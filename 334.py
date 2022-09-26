import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minn = sys.maxsize
        min_second = sys.maxsize

        for num in nums:
            if num <= minn:
                minn = num
            elif num <= min_second:
                min_second = num
            else:
                return True
        return False
