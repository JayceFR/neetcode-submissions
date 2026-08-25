# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        prev, curr = None, head 

        length = 0 
        lcurr = head 
        while lcurr != None:
            length += 1 
            lcurr = lcurr.next 
        
        node = ListNode()
        nh = node 
        last = None
        for x in range(length // k):
            last = curr 
            for y in range(k):
                # reverse it 
                nc = curr.next 
                curr.next = prev 
                prev, curr = curr, nc 
            node.next = prev 
            prev = None 
            node = last 
        # add remaining items 

        while curr is not None:
            node.next = curr 
            node = node.next 
            curr = curr.next 

        return nh.next 