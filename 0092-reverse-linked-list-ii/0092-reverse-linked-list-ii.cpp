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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode*lft=head;
        ListNode*lftprev=NULL;
        ListNode*rght=head;
        int n=1;
        while(n!=left)
        {   lftprev=lft;
            lft=lft->next;
            n++;
        }
        n=1;
        while(n!=right)
        {   
            rght=rght->next;  
            n++;        
        }
        
        
        ListNode* stop = rght->next;
        ListNode*prev=NULL;
        ListNode*curr=lft;
         while (curr != stop) {
            ListNode* next = curr->next;

            curr->next = prev;

            prev = curr;
            curr = next;
        }
        if (lftprev != NULL)
            lftprev->next = rght;
        else
            head = rght;

        lft->next = curr;

        return head;
        
    }
};