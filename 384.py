import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.org_nums = nums.copy()
        self.new_nums = nums.copy()

    def reset(self) -> List[int]:
        return self.org_nums.copy()

    def shuffle(self) -> List[int]:
        random.shuffle(self.new_nums)
        return self.new_nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
