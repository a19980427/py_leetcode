class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0

        depth = 0
        stack = []

        for i in range(len(s)):
            ch = s[i]

            if ch == '(':
                depth += 1
                res = max(res, depth)
                stack.append(ch)
            elif ch == ')':
                while stack.pop() != '(':
                    pass
                depth -= 1
            else:
                stack.append(ch)
        return res


a = Solution()
a.maxDepth("(1+(2*3)+((8)/4))+1")
