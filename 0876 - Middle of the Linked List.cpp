/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int length = 0;
        struct ListNode* new_head = head;
        while(new_head){new_head = new_head->next; length++;}
        length >>= 1;
        new_head = head;
        int i = 0;
        while(length--){new_head = new_head->next;}
        return new_head;
        }
};