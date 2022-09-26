import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_map = [0] * 26
        magazine_map = [0] * 26

        self.count(ransomNote_map, ransomNote)
        self.count(magazine_map, magazine)

        for i in range(26):
            if magazine_map[i] - ransomNote_map[i] < 0:
                return False
        return True

    def count(self, cnt_map, string):
        for ch in string:
            index = ord(ch) - ord('a')
            cnt_map[index] += 1
