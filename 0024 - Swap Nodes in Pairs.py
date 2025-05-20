# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = head
        nodes = []
        while new_head:
            nodes.append(new_head)
            new_head = new_head.next
        i = 0
        while i <= len(nodes) - 2:
            nodes[i], nodes[i + 1] = nodes[i + 1], nodes[i]
            i += 2

        head = nodes[0]
        curr_head = head
        for i in range(1, len(nodes)):
            curr_head.next = nodes[i]
            curr_head = nodes[i]
        curr_head.next = None
        return head