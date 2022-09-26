import collections


class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0

        cnt = [0] * 26
        res = 1
        pre_ch = s[0]
        for ch in s:
            index = ord(ch) - ord('a')
            if ch == pre_ch:
                cnt[index] += 1
                res = max(res, cnt[index])
            else:
                cnt[index] = 1
        return res