# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1, list2 = [], []

        def leaves(root, _list):
            if root and root.left is None and root.right is None:
                _list.append(root.val)
                return
            if root.left is not None:
                leaves(root.left, _list)
            if root.right is not None:
                leaves(root.right, _list)

        leaves(root1, list1)
        leaves(root2, list2)
        return list1 == list2