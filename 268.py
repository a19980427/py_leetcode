class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        res = n * (1 + n) / 2 - sum(nums)
        return int(res)
