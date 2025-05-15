/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    int length = 0;
    struct ListNode* new_head = head;
    while(new_head){new_head = new_head->next; length++;}
    length >>= 1;
    new_head = head;
    int i = 0;
    while(length--){new_head = new_head->next;}
    return new_head;
}