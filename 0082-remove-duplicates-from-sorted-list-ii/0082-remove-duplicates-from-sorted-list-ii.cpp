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

        
        while (head != NULL && head->next != NULL &&
               head->val == head->next->val) {

            int value = head->val;

            while (head != NULL && head->val == value) {
                head = head->next;
            }
        }

        if (head == NULL)
            return NULL;

        ListNode* temp = head;

        while (temp->next != NULL) {

            if (temp->next->next != NULL &&
                temp->next->val == temp->next->next->val) {

                int value = temp->next->val;

                while (temp->next != NULL &&
                       temp->next->val == value) {
                    temp->next = temp->next->next;
                }

            } else {
                temp = temp->next;
            }
        }

        return head;
    }
};