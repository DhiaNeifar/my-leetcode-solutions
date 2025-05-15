# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head
        length = 0
        while new_head:
            length += 1
            new_head = new_head.next
        second_half = length // 2
        new_head = head
        i = 0
        while i < second_half:
            new_head = new_head.next
            i += 1
        return  new_head