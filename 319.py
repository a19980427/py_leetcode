class Solution:
    def bulbSwitch(self, n: int) -> int:
        arr = [False] * n

        for gap in range(1, n+1):
            for i in range(gap-1, n, gap):
                arr[i] = not arr[i]
        res = arr.count(True)
        return res
