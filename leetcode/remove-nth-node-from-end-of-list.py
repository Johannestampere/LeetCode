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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = new ListNode(0, head);
        ListNode* L = temp;
        ListNode* R = temp;

        for (int i=0; i <= n; ++i) {
            R = R->next;
        }

        while (R) {
            L = L->next;
            R = R->next;
        }

        L->next = L->next->next;

        return temp->next;
    }
};