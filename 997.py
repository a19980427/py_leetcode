from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = [0] * (n + 1)
        trusted_map = [0] * (n + 1)

        for elem in trust:
            trust_p = elem[0]
            trusted_p = elem[1]

            # 这个人信任的多少个人
            trust_map[trust_p] += 1
            # 这个人被多少人信任
            trusted_map[trusted_p] += 1

        for i in range(1, n + 1):
            if trust_map[i] == 0 and trusted_map[i] == n - 1:
                return i
        return -1


a = Solution()
res = a.findJudge(3, [[1, 3], [2, 3]])
