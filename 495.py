class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        res = duration
        for i in range(1, len(timeSeries)):
            gap = timeSeries[i] - timeSeries[i - 1]
            res += min(duration, gap)
        return res
