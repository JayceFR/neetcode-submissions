# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Basically split and merge 
        def kmerge(klist):
            if len(klist) == 0:
                return None 
            if len(klist) == 1:
                return klist[0]
            if len(klist) == 2:
                return self.mergeTwoLists(klist[0], klist[1])
            
            llist = klist[0:len(klist)//2]
            rlist = klist[len(klist)//2:]
            sllist = kmerge(llist)
            srlist = kmerge(rlist) 

            return self.mergeTwoLists(sllist, srlist)

        
        flist = kmerge(lists)
        return flist  
            

        