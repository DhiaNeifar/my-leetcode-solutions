# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        
        while temp:
            length += 1
            temp = temp.next
        
        index = length - n

        if index == 0:
            new_head = head.next
            del head
            return new_head
        
        prev = None
        curr = head
        i = 0

        while curr and i < index:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next
        del curr

        return head