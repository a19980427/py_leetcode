from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        length = len(security)
        max_arr = [security[0]] * length
        min_arr = [security[0]] * length

        for i in range(1, length):
            max_arr[i] = max(max_arr[i - 1], security[i])
            min_arr[i] = min(min_arr[i - 1], security[i])

        left = 0
        right = left + time + 1 + time

        while right < length:
            # 左边不是递增: 两端分别不是最小值和最大值
            if min_arr[left] != min_arr[left - 1] and max_arr[left + time] != max_arr[left + time - 1]:


arr = [5, 3, 3, 3, 5, 6, 2]
a = Solution()
a.goodDaysToRobBank(arr, 2)
