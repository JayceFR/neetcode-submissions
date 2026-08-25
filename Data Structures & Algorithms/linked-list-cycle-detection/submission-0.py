# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head):

        seen = set([])
        def cycle(curr):
            if curr is None:
                return False 
            if curr.val in seen:
                return True
            seen.add(curr.val)
            return cycle(curr.next)
        
        return cycle(head)


        
        