import collections
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_cnt = collections.Counter(nums)
        if len(num_cnt) == 0 or len(num_cnt) == 1:
            return 0
        nums = num_cnt.keys()
        sort_nums = sorted(nums)
        res = 0
        for i in range(1, len(sort_nums)):
            if sort_nums[i] == sort_nums[i - 1] + 1:
                res = max(res, num_cnt[sort_nums[i]] + num_cnt[sort_nums[i - 1]])
        return res
