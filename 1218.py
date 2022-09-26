class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        res_map = {}
        for i in arr:
            if i - difference in res_map:
                res_map[i] = res_map[i - difference] + 1
            else:
                res_map[i] = 1
        return max(res_map.values())


a = Solution()
a.longestSubsequence(arr=[1, 2, 3, 4], difference=1)
