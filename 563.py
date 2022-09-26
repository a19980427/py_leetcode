# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.depth_sum = 0
        self.search(root)
        return self.depth_sum

    def search(self, root):
        if root is None:
            return 0
        left_sum = self.search(root.left)
        right_sum = self.search(root.right)
        self.depth_sum += abs(left_sum - right_sum)
        return root.val + left_sum + right_sum
