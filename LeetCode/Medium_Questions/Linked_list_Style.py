# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d={}
        while(1):
            if(head==None):
                return False
            if(head.next==None):
                return False
            if(head in d):
                return True
            else:
                d[head]=True
                head=head.next
