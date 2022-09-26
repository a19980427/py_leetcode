from typing import List


# 输入：richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
# 输出：[5,5,2,5,4,5,6,7]
#
# 链接：https://leetcode-cn.com/problems/loud-and-rich


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        length = len(quiet)
        res = [0] * length

        richer_map = {i: [] for i in range(length)}
        for item in richer:
            rich = item[0]
            poor = item[1]
            richer_map[poor].append(rich)

        print(richer_map)

        for i in range(length):
            i_richer = self.findMoreRich(i, richer_map)
            print(i_richer)
            i_richer_quiet = [(i, quiet[i]) for i in i_richer]
            i_richer_quiet.sort(key=lambda x: x[1])
            res[i] = i_richer_quiet[0][0]
        return res

    def findMoreRich(self, poor_index, richer_map):
        print("-------poor index ------------ ")
        i_richer = set()
        queue: List = richer_map[poor_index].copy()
        i_richer.add(poor_index)
        while queue:
            person = queue.pop(0)
            i_richer.add(person)
            for p in richer_map[person]:
                if p not in i_richer:
                    queue.append(p)
        return i_richer


a = Solution()
res = a.loudAndRich(richer=[[0, 1], [1, 2]], quiet=[0, 1, 2])
print(res)
