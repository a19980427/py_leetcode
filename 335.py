class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        lens = len(distance)

        if lens < 4:
            return False
        i = 3
        while i < lens:
            if (distance[i] >= distance[i - 2]) and (distance[i - 3] >= distance[i - 1]):
                return True
            if i >= 4:
                if (distance[i] + distance[i - 4] == distance[i - 2]) and (distance[i - 3] == distance[i - 1]):
                    return True
            if i >= 5:
                if (distance[i] + distance[i - 4] >= distance[i - 2]) and \
                        (distance[i - 5] + distance[i - 1] >= distance[i - 3]) and \
                        (distance[i - 3] > distance[i - 1]) and (distance[i - 2] > distance[i - 4]):
                    return True
            i += 1
        return False


a = Solution()
print(a.isSelfCrossing([1, 1, 2, 2, 1, 1]))
