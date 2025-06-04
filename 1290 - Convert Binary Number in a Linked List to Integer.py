# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = head
        result = 0
        while curr:
            result *= 2
            result += curr.val
            curr = curr.next
        return result