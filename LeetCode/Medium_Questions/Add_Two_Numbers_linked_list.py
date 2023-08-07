class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        temp = l3
        carry = 0
        
        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            sum1 = val1 + val2 + carry
            carry = sum1 // 10
            value = sum1 % 10
            
            temp.next = ListNode(value)
            temp = temp.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        if carry != 0:
            temp.next = ListNode(carry)
            
        return l3.next
