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
        copy = Node(0)
        curr_c = copy 
        curr_h = head 
        map = {}
        while curr_h is not None:
            curr_c.next = Node(curr_h.val)
            map[curr_h] = curr_c.next
            curr_h = curr_h.next 
            curr_c = curr_c.next 
        
        curr_c = copy.next 
        curr_h = head 

        while curr_h is not None:
            if curr_h.random is None:
                curr_c.random = None 
            else:
                curr_c.random = map[curr_h.random]

            curr_h = curr_h.next 
            curr_c = curr_c.next 

        return copy.next 