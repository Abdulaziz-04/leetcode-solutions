# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev,curr=None,slow.next
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        mxSum=0
        curr=head
        while prev and curr:
            mxSum=max(mxSum,prev.val+curr.val)
            prev=prev.next
            curr=curr.next
        return mxSum


        