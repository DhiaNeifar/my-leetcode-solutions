# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        ToMeasureLength = head
        while ToMeasureLength:
            ToMeasureLength = ToMeasureLength.next
            length += 1
        if length == 1:
            return head
        
        index = length - k

        
        swap1 = head
        i = 0
        while swap1 and i < k - 1:
            swap1 = swap1.next
            i += 1

        swap2 = head
        i = 0
        while swap2 and i < index:
            swap2 = swap2.next
            i += 1
                
        swap1.val, swap2.val = swap2.val, swap1.val
        return head