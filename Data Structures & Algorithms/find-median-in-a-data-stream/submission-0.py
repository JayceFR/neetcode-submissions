import heapq as h 
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            h.heappush(self.large, num)
        else:
            h.heappush(self.small, num * -1)
        
        if len(self.small) > len(self.large) + 1:
            val = h.heappop(self.small) * -1 
            h.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = h.heappop(self.large) * -1
            h.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2.0 
        
        