# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # our second half is from slow.next 
        # reverse the second half 
        prev, curr = None, slow.next 
        while curr is not None:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        slow.next = prev 

        # merge both the lists 
        first, second = head, slow.next 
        slow.next = None 
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1 
            first, second = tmp1, tmp2 

