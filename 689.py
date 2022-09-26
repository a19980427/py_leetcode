from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        sum_k = [0] * length
        sum_k[k - 1] = sum(nums[0:k])

        start = k
        while start < length:
            sum_k[start] = sum_k[start - 1] + nums[start] - nums[start - k]
            start += 1

        print(sum_k)


a = Solution()
a.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], k=2)
