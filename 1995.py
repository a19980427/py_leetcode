from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0

        for i in range(length - 3):
            for j in range(i + 1, length - 2):
                for k in range(j + 1, length - 1):
                    sum = nums[i] + nums[j] + nums[k]
                    for y in range(k + 1, length):
                        target = nums[y]
                        if sum == target:
                            res += 1
        return res
