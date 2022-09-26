from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        sums = [0] * (len(nums1) * len(nums2))
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sums[i * len(nums2) + j] = nums1[i] + nums2[j]

        sorted_sums = sorted(enumerate(sums), key=lambda x: x[1])
        res = []
        for i in range(k):
            if i >= len(sorted_sums):
                break
            index, val = sorted_sums[i]
            nums1_index = index // len(nums2)
            nums2_index = index % len(nums2)
            res.append([nums1[nums1_index], nums2[nums2_index]])
        return res


a = Solution()
a.kSmallestPairs([1, 2],
                 [3],
                 3)
