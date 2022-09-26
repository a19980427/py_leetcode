from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        sort_nums = sorted(nums, key=lambda x: abs(x), reverse=True)

        i = 0
        while i < len(sort_nums) and k > 0:
            if sort_nums[i] < 0:
                sort_nums[i] = - sort_nums[i]
                k -= 1
            i += 1

        if k % 2 == 1:
            sort_nums[i - 1] = -sort_nums[i - 1]
        return sum(sort_nums)
