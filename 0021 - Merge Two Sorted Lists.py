# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        l3 = ListNode()
        if (l1.val < l2.val):
            l3.val = l1.val
            l1 = l1.next
        else :
            l3.val = l2.val
            l2 = l2.next
        curr = l3
        while (l1 != None and l2 != None):
            if (l1.val < l2.val):
                new = ListNode(l1.val, None)
                l1 = l1.next
            else:
                new = ListNode(l2.val, None)
                l2 = l2.next
            curr.next = new
            curr = new
        while(l1 != None):
            new = ListNode(l1.val, None)
            l1 = l1.next
            curr.next = new
            curr = new
        while(l2 != None):
            new = ListNode(l2.val, None)
            l2 = l2.next
            curr.next = new
            curr = new
        return l3