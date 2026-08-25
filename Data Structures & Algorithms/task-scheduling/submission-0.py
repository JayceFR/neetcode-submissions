import heapq as h 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # A A A B C 
        # A : 3, B : 1, C : 1 
        # count the frequency of each character 
        count = {}
        for c in tasks:
            count[c] = count.get(c, 0) + 1
        
        # create a heap with the data 
        # (frequency, time)
        heap = []
        for k, v in count.items():
            h.heappush(heap, (-v,1))
        
        time = 1
        while len(heap) > 0:
            print(heap)
            old = []
            curr = h.heappop(heap)
            while curr[1] > time and heap:
                old.append(curr)
                curr = h.heappop(heap)
            
            
            # append the old back in 
            for item in old:
                h.heappush(heap, item)
            
            if curr[1] > time:
                h.heappush(heap, curr)
                time += 1 
                continue 
            
            # modify current 
            if (curr[0] * -1) > 1:
                # need to add it back in
                h.heappush(heap, (curr[0] + 1, time + 1 + n))

            time += 1 
        return time - 1 
        

