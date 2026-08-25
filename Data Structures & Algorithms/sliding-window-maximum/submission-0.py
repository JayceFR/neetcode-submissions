import heapq as h 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for i in range(len(nums)):
            h.heappush(heap, (-nums[i], i))
            if i >= k -1:
                while heap[0][1] <= i - k:
                    h.heappop(heap)
                result.append(-heap[0][0])
        h.heappop(heap)
        return result