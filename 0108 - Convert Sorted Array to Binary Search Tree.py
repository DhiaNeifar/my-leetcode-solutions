# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def CreateBST(table, start, end):
            if start > end:
                return None
            mid = (end + start) // 2
            return TreeNode(val=table[mid], left=CreateBST(nums, start, mid - 1), right=CreateBST(nums, mid + 1, end))
        
        return CreateBST(nums, 0, len(nums) - 1)