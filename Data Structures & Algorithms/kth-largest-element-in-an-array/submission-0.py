import heapq as h 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        h.heapify(heap)
        print(h.nlargest(k,heap))
        return h.nlargest(k, heap)[-1]