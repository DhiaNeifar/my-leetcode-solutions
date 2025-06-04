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
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head) return head;
        ListNode* left = head;
        ListNode* right, to_delete;
        while(left){
            right = left->next;            
            while(right && right->val == left->val){
                right = right->next;
            }
            left->next = right;
            left = right;
        }
        return head;
    }
};