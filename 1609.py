from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        self.vals = []
        self.level_search(root, 0)
        for index, val in enumerate(self.vals):
            flag = index % 2

            if val[0] % 2 == flag:
                return False

            # 奇数下标,所有数都是偶数,严格递减
            if flag == 1:
                for i in range(1, len(val)):
                    if val[i - 1] <= val[i] or val[i] % 2 == flag:
                        return False

            # 偶数下标,所有数都是奇数,严格递增
            if flag == 0:
                for i in range(1, len(val)):
                    if val[i - 1] >= val[i] or val[i] % 2 == flag:
                        return False
        return True

    def level_search(self, root, level):
        if root is None:
            return
        if len(self.vals) <= level:
            self.vals.append([])
        self.vals[level].append(root.val)
        self.level_search(root.left, level + 1)
        self.level_search(root.right, level + 1)
