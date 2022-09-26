# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        root_val = root.val
        if val == root_val:
            return root
        elif val > root_val and root.right is not None:
            return self.searchBST(root.right, val)
        elif val < root_val and root.left is not None:
            return self.searchBST(root.left, val)
