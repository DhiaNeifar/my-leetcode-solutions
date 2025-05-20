# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lengths = [GetLength(linked_list) for linked_list in lists]
        result_length = sum(lengths)
        if result_length == 0:
            return None

        curr_result_length = 0
        result_head = ListNode()
        result = result_head
        while curr_result_length < result_length:
            curr_min, index = float("inf"), len(lists)
            for head_index, head in enumerate(lists):
                if head and head.val < curr_min:
                    curr_min = head.val
                    index = head_index
            result.val = curr_min
            lists[index] = lists[index].next
            if not curr_result_length == result_length - 1:
                result.next = ListNode()
            result = result.next
            curr_result_length += 1
        return result_head

def GetLength(head: Optional[ListNode]):
    new_head = head
    length = 0
    while new_head:
        length += 1
        new_head = new_head.next
    return length