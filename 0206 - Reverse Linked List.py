# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1 = head
        if not head:
            return node1
        
        node2 = node1.next
        if not node2:
            return head
        
        node3 = node2.next
        if not node3:
            node1.next = None
            node2.next = node1
            return node2

        node1.next = None
        while node3:
            node2.next = node1
            node1 = node2
            node2 = node3
            node3 = node3.next
        
        node2.next = node1
        return node2