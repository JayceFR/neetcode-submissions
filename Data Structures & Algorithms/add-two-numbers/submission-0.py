# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def add(self, l1, l2, carry, out):
        if l1 == None and l2 == None and carry == 0:
            return 
        val = 0 
        if l1 != None:
            val += l1.val 
        if l2 != None:
            val += l2.val 
        val += carry 
        out.next = ListNode(val % 10)
        
        newCarry = val // 10 
        if l1 == None:
            if l2 == None:
                if newCarry != 0:
                    self.add(None, None, newCarry, out.next)
                # else we don't do anything, we are done 
            else:
                self.add(None, l2.next, newCarry, out.next)
        else:
            if l2 == None:
                self.add(l1.next, None, newCarry, out.next)
            else:
                self.add(l1.next, l2.next, newCarry, out.next)
        

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0) #dummy node 
        self.add(l1, l2, 0, head)
        return head.next 
        