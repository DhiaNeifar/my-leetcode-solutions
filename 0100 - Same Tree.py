# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def CheckTree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None and node2 is not None:
                return False
            if node1 is not None and node2 is None:
                return False
            return node1.val == node2.val and CheckTree(node1.left, node2.left) and CheckTree(node1.right, node2.right)
        return CheckTree(p, q)