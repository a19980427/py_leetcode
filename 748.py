from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate_map = self.get_alpha_map(licensePlate)

        min_length = 10000
        res = 0
        for i in range(len(words)):
            word_map = self.get_alpha_map(words[i])
            length = len(words[i])
            minus = [j - i for i, j in zip(licensePlate_map, word_map)]
            if min(minus) >= 0 and min_length > length:
                res = i
                min_length = length
        return words[res]

    def get_alpha_map(self, string):
        cnt_map = [0] * 26
        for ch in string:
            ch = str.lower(ch)
            if ch.isalpha():
                index = ord(ch) - ord('a')
                cnt_map[index] += 1
        return cnt_map


a = "123"
print(a.lower())
