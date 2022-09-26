# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.search(root, res)
        return res

    def search(self, root, res: List[int]):
        if root is None:
            return
        res.append(root.val)
        for child in root.children:
            self.search(child, res)
