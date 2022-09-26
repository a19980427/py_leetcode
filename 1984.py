from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        sort_nums = sorted(nums)

        min_val = 100000000
        for i in range(k - 1, len(sort_nums)):
            print(sort_nums[i], sort_nums[i - k - 1])
            min_val = min(min_val, sort_nums[i] - sort_nums[i - k + 1])
        print(min_val)
        return min_val


# 1 4 7 9
a = Solution()
a.minimumDifference([9, 4, 1, 7]
                    , 2)
