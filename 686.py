class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        set_a = set(a)
        set_b = set(b)

        if set_b <= set_a:
            b_length = len(b)
            a_length = len(a)

            times = 1
            temp = a * times
            t_length = len(temp)

            while t_length < 2 * a_length + b_length:
                if temp.find(b) != -1:
                    return times
                times += 1
                temp = a * times
                t_length = len(temp)
            return -1
        else:
            return -1


a = Solution()
a.repeatedStringMatch(
    "abcd",
    "cdabcdab")
