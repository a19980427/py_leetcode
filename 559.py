# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # 上层有多少个父节点,下层就有多少个null(最后一层除外)
        return self.search(root)

    def search(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.search(child))
        return max_depth
