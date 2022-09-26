import string


class Solution:
    def modifyString(self, s: str) -> str:
        pre = -1
        nex = -1

        res = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                # 取得前缀
                if i - 1 >= 0:
                    pre = res[i - 1]
                else:
                    pre = '#'
                # 取得后缀
                if i + 1 < len(s):
                    nex = res[i + 1]
                else:
                    nex = '#'
                res[i] = self.get_one(pre, nex)
        return ''.join(res)

    def get_one(self, pre, nex):
        for ch in string.ascii_lowercase:
            if ch != pre and ch != nex:
                return ch
