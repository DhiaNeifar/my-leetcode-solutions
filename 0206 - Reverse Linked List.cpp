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
    ListNode* reverseList(ListNode* head) {
        vector<int> values;
        ListNode* other = head;

        while(other){
            values.push_back(other->val);
            other = other->next;
        }

        other = head;

        int index = values.size() - 1;
        while(other){
            other->val = values[index];
            other = other->next;
            index--;
        }

        return head;
    }
};