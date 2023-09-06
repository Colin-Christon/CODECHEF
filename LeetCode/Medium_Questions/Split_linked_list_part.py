# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the length of the linked list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        # Step 2: Calculate the size of each part and the number of parts with extra nodes
        part_size = length // k
        extra_nodes = length % k
        
        result = []
        temp = head
        
        for _ in range(k):
            part_head = temp  # Start of the current part
            part_length = part_size + (1 if extra_nodes > 0 else 0)  # Calculate the part length
            
            if part_head:
                # Traverse the current part
                for _ in range(part_length - 1):
                    temp = temp.next
                
                # Disconnect the current part from the next
                next_temp = temp.next
                temp.next = None
                temp = next_temp
                
                extra_nodes -= 1
            
            result.append(part_head)
        
        return result

            
        
        
