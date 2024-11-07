# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKthNode(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(-1,head)
        gPrev=dummy
        while True:
            kNode=self.getKthNode(gPrev,k)
            if not kNode:
                break
            gNext=kNode.next
            prev,curr=kNode.next,gPrev.next
            while curr!=gNext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp

            tmp=gPrev.next
            gPrev.next=kNode
            gPrev=tmp
        return dummy.next


        