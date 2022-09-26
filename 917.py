class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)

        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
            if left < right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
        return "".join(s)


a = Solution()
a.reverseOnlyLetters(s="ab-cd")
