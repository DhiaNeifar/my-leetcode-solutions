# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        middle = prev
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        middle.next = prev
        twin = middle.next

        start = head
        curr_max = 0

        while twin:
            new_val = start.val + twin.val
            curr_max = max(curr_max, start.val + twin.val)
            twin = twin.next
            start = start.next
        return curr_max