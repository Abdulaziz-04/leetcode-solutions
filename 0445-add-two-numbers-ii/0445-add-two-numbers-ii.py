# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_stack(ll):
            stack=[]
            curr=ll
            while curr:
                stack.append(curr.val)
                curr=curr.next
            return stack
        s1,s2=get_stack(l1),get_stack(l2)
        carry=0
        result=ListNode()
        while s1 or s2 or carry:
            v1=s1.pop() if s1 else 0
            v2=s2.pop() if s2 else 0
            total=v1+v2+carry
            carry=total//10
            result.val=total%10
            head=ListNode(carry)
            head.next=result
            result=head
        return result.next if carry==0 else result
        


        

        