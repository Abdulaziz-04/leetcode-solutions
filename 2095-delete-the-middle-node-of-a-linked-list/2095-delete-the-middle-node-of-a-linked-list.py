# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return None
        dummy=ListNode(-1,head)
        slow,fast=dummy,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head
        