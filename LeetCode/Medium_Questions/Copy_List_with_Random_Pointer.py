"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node_mapping = {}
        temp = head

        # First pass: Create a new node for each original node, and map them
        while temp:
            node_mapping[temp] = Node(temp.val)
            temp = temp.next

        # Second pass: Link the copied nodes, including the random pointers
        temp = head
        while temp:
            copied_node = node_mapping[temp]
            copied_node.next = node_mapping.get(temp.next)
            copied_node.random = node_mapping.get(temp.random)
            temp = temp.next

        # Return the head of the copied linked list
        return node_mapping[head]

