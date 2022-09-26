from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_release_time = -1
        res = 'a'
        pre = 0
        for i in range(len(releaseTimes)):
            release_time = releaseTimes[i] - pre
            pre = releaseTimes[i]
            key = keysPressed[i]
            if release_time > max_release_time:
                max_release_time = release_time
                res = key
            elif release_time == max_release_time:
                res = chr(max(ord(res), ord(key)))

            print(f"releasetime {release_time} key {key} ")
        print(res)
        return res

    def slowestKey1(self, releaseTimes: List[int], keysPressed: str) -> str:
        print([0] + releaseTimes)
        print(releaseTimes)
        for b, c, in zip(map(int.__sub__, releaseTimes, [0] + releaseTimes), keysPressed):
            print(b, c)

        return max(zip(map(int.__sub__, releaseTimes, [0] + releaseTimes), keysPressed))[1]


a = Solution()
a.slowestKey1([12, 23, 36, 46, 62],
              "spuda")
