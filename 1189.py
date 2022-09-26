class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ch_map = [0] * 26
        for ch in text:
            ch_map[self.get_index(ch)] += 1

        return min(ch_map[self.get_index('b')], ch_map[self.get_index('a')], ch_map[self.get_index('l')] / 2,
                   ch_map[self.get_index('o')] / 2, ch_map[self.get_index('n')], )

    def get_index(self, ch):
        return ord(ch) - ord('a')
