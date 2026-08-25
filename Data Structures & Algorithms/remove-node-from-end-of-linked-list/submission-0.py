# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0 
        curr = head 
        while curr is not None:
            length += 1 
            curr = curr.next 
        
        iterate = length - n 
        if iterate == 0:
            return head.next 
        curr = head 
        for x in range(iterate - 1):
            curr = curr.next 
        
        # now need to remove curr.next 
        curr.next = curr.next.next 
        return head 