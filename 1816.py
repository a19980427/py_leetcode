class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        if not s:
            return ""
        space = 0
        index = 0
        for i in range(len(s)):
            ch = s[i]
            if ch == ' ':
                space += 1
                if space == k:
                    return s[:i]
        return s


