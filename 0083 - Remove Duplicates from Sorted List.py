# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original_head = head
        while head is not None:
            block = head.next
            while block is not None and block.val == head.val:
                block = block.next
            head.next = block
            head = block
        return original_head