# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        freq = {}
        curr = head
        while curr:
            freq[curr.val] = freq.get(curr.val, 0) + 1
            curr = curr.next
        unique_values = sorted([unique_value for unique_value in freq if freq[unique_value] == 1])

        if not unique_values:
            return None

        prev = None
        curr = head
        for unique_value in unique_values:
            prev = curr
            curr.val = unique_value
            curr = curr.next

        curr = prev
        to_delete = curr
        curr.next = None

        return head