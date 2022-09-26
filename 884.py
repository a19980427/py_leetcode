import collections
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        count = collections.Counter(A.split() + B.split())
        return [k for k, v in count.items() if v == 1]