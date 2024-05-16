# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Reverse linked list after the mid point
        slow=head
        fast=head
        n=0
        while fast and fast.next:
            slow=slow.next
            n+=1
            fast=fast.next.next
        prev=None
        cur=slow
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        end=prev
        start=head
        l=0
        mx_val=0
        while l!=n:
            mx_val=max(end.val+start.val,mx_val)
            end=end.next
            start=start.next
            l+=1
        return mx_val

        
        