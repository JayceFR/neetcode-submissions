# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        finalList = ListNode()
        def merge(a, b, curr):
            
            if a is None:
                if b is None:
                    return 
                else:
                    curr.next = b 
                    return 
            else:
                if b is None:
                    curr.next = a 
                    return 
                if a.val < b.val:
                    curr.next = ListNode(a.val)
                    merge(a.next, b, curr.next)
                else:
                    curr.next = ListNode(b.val)
                    merge(a, b.next, curr.next)
        
        merge(list1, list2, finalList)
        return finalList.next 

        