from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_len = len(p)
        s_len = len(s)

        if s_len < p_len:
            return res

        p_cnt_map = self.get_cnt_map(p)
        start_index = 0
        s_cnt_map = self.get_cnt_map(s[0:p_len - 1])

        while start_index + p_len <= s_len:
            # 将最后一个元素加入到字典中
            end_index = start_index + p_len - 1
            end_ch = s[end_index]
            end_map_index = ord(end_ch) - ord('a')
            s_cnt_map[end_map_index] += 1

            if s_cnt_map == p_cnt_map:
                res.append(start_index)

            # 删除第一个元素
            start_ch = s[start_index]
            start_map_index = ord(start_ch) - ord('a')
            s_cnt_map[start_map_index] -= 1

            start_index += 1
        return res

    def get_cnt_map(self, string):
        cnt_map = [0] * 26
        for ch in string:
            index = ord(ch) - ord('a')
            cnt_map[index] += 1
        return cnt_map


a = Solution()
print(a.findAnagrams(
    "abab",
    "ab"))
