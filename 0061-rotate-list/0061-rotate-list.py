# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
       
        if k==0:
            return head
        n = 1

       
        temp=head
        while temp.next!=None:
            temp=temp.next
            n+=1
        k = k % n
        for i in range(k):
            temp = head

            while temp.next.next != None:
                temp = temp.next

            last = temp.next
            temp.next = None

            last.next = head
            head = last
          

        return head
