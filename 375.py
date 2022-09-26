class Solution:
    def getMoneyAmount(self, n: int) -> int:
        self.dict = {}
        return self.search(0, n)

    def search(self, left, right):
        if right <= left:
            return 0

        if self.dict.get((left, right), False):
            return self.dict.get((left, right))

        # split_index = self.find_split_index(nums)
        max_cost = float('inf')

        for split_index in range(left, right + 1):
            cost = split_index
            cost += max(self.search(left, split_index - 1), self.search(split_index + 1, right))
            max_cost = min(max_cost, cost)
        self.dict[(left, right)] = max_cost

        return max_cost
