from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        strings = text.split()
        print(strings)
        res = []

        for i in range(len(strings) - 2):
            first_string = strings[i]
            second_string = strings[i + 1]

            if first == first_string and second == second_string:
                res.append(strings[i + 2])

        return res
