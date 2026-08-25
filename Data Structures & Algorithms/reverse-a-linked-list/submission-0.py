# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None 
        if head.next == None:
            return head 
        rList = self.reverseList(head.next)
        # add head.val to end of list 
        curr = rList
        while curr.next != None:
            curr = curr.next 
        #detach head
        head.next = None 
        curr.next = head
        return rList
        