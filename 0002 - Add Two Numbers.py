# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        integer1, integer2, min_length, l1_length, l2_length = 0, 0, 0, 0, 0
        l11, l22 = l1, l2
        while l11 and l22:
            integer1, integer2 = l11.val * pow(10, min_length) + integer1, l22.val * pow(10, min_length) + integer2
            l11, l22 = l11.next, l22.next
            min_length += 1
    
        while l11:
            integer1 = l11.val * pow(10, min_length + l1_length) + integer1
            l11 = l11.next
            l1_length += 1
            
        while l22:
            integer2 = l22.val * pow(10, min_length + l2_length) + integer2
            l22 = l22.next
            l2_length += 1
            
        final_sum = integer1 + integer2 
        
        l3 = ListNode(final_sum % 10, next=None)
        l33 = l3
        final_sum //= 10
        while final_sum:
            l4 = ListNode(final_sum % 10, None)
            l33.next = l4
            l33 = l33.next
            final_sum //= 10
        return l3