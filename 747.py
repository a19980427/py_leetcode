from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max = -1
        max_index = -1

        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                max_index = i

        for i in range(len(nums)):
            if i != max_index:
                if max < 2 * nums[i]:
                    return -1

        return max_index
