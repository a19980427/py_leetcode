import collections


class Solution:

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s_map = self.get_map(s)
        goal_map = self.get_map(goal)

        exchange = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                s_map_index = s_map[self.ascii(goal[i])]
                goal_map_index = goal_map[self.ascii(s[i])]

                print(s_map_index)
                print(goal_map_index)

                if len(set(s_map_index) & set(goal_map_index)) >= 1:
                    exchange += 1
        return exchange == 2

    def get_map(self, string):
        map = [[] for i in range(26)]
        for index in range(len(string)):
            ch = string[index]
            map[self.ascii(ch)].append(index)
        return map

    def ascii(self, ch):
        return int(ord(ch) - ord('a'))


a = Solution()
res = a.buddyStrings("aa", "aa")
print(res)
