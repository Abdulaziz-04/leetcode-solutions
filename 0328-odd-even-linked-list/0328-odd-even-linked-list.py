# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        odd=ListNode(-1)
        even=ListNode(-1)
        o_head=odd
        e_head=even
        curr=head
        i=1
        while curr:
            if i%2==0:
                even.next=ListNode(curr.val,None)
                even=even.next
            else:
                odd.next=ListNode(curr.val,None)
                odd=odd.next
            i+=1
            curr=curr.next
        odd.next=e_head.next
        return o_head.next



        