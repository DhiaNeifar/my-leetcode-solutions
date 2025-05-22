# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        for i in range(len(stack) // 2):
            if stack[i] != stack[len(stack) - i - 1]:
                return False
        return True