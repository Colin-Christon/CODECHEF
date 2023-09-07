# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        current = prev.next
        next_node = current.next

        for _ in range(right - left):
            temp = next_node.next
            next_node.next = current
            current = next_node
            next_node = temp

        prev.next.next = next_node
        prev.next = current
        
        return dummy.next


        
