# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], target: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if curr.val == target:
                prev.next = curr.next
                to_delete = curr
                del to_delete
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next
        """if not head:
            return None
        
        vals = []
        curr = head
        while curr:
            if curr.val != target:
                vals.append(curr.val)
            curr = curr.next
        
        curr = head

        prev = None
        for val in vals:
            curr.val = val
            prev = curr
            curr = curr.next
        if not prev:
            return None

        prev.next = None
        return head
"""