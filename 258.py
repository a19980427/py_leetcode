class Solution:
    def addDigits(self, num: int) -> int:
        n_sum, length = self.get_Sum(num)
        while length > 1:
            n_sum, length = self.get_Sum(n_sum)
        return n_sum




    def get_Sum(self, num):
        str_num = str(num)
        length = len(str_num)

        n_sum = 0
        for i in range(length):
            n_sum += int(str_num[i])

        return n_sum, len(str(n_sum))
