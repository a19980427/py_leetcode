from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        int_times = [self.toInt(timePoint) for timePoint in timePoints]
        sort_times = sorted(int_times)
        minute = 1500
        for i in range(1, len(sort_times)):
            gap = (sort_times[i][0] - sort_times[i - 1][0]) * 60 + (sort_times[i][1] - sort_times[i - 1][1])
            minute = min(gap, minute)
        # 开始和结尾时间
        minute = min(minute,
                     1440 - ((sort_times[-1][0] - sort_times[0][0]) * 60 + sort_times[-1][1] - sort_times[0][1]))
        return minute

    def toInt(self, time):
        hh, mm = time.split(':')
        hh = int(hh)
        mm = int(mm)
        return hh, mm
