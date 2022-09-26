class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.search(root, res)
        return res

    def search(self, root, res):
        if root is not None:
            for child in root.children:
                self.search(child, res)
            res.append(root.val)
