# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if(head==None):
            return head
        temp=head
        prev=ListNode(0,head)
        head2=prev
        while(temp!=None):
            if(temp.val==val):
                prev.next=temp.next
            else:
                prev=temp
            temp=temp.next
        return head2.next
