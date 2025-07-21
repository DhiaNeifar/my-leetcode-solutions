# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + Solution.minDepth(self, root.right)
        if not root.right:
            return 1 + Solution.minDepth(self, root.left)
        return 1 + min(Solution.minDepth(self, root.left), Solution.minDepth(self, root.right))