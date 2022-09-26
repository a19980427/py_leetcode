class Solution:

    def check(self, string):
        cnt = 0
        for i in string:
            if i == "(":
                cnt += 1
            elif i == ")":
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    def removeInvalidParentheses(self, s: str):
        level = {s}
        while True:
            valid = list(filter(self.check, level))
            if valid:
                return valid
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in ["(", ")"]:
                        next_level.add(string[:i] + string[i + 1:])
            level = next_level


a = Solution()
print(a.removeInvalidParentheses("(r(()()("))
