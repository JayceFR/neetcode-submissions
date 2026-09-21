import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ts = []
        for pos, task in enumerate(tasks):
            ts.append((task[0], task[1], pos))
        # print(ts) # (start_time, end_time, index)

        heapq.heapify(ts)
        res = []
        time = 0

        while ts:
            st, et, i = heapq.heappop(ts)
            time = max(time, st)
            # need to pop other possibilities, we can select from 
            poss = [(st,et,i)]
            minpos = 0 
            minet = et 
            pos = 1
            while ts and ts[0][0] <= time:
                # its a possibility. 
                cst, cet, ci = heapq.heappop(ts)
                poss.append((cst, cet, ci))
                if cet < minet:
                    minet = cet
                    minpos = pos 
                pos +=1 
                
            # print("Poss for time t", time, "are:", poss)
            # need to get the element with the minet 
            st, et, i = poss.pop(minpos)
            time = time + et 
            res.append(i)
            # Now add all other poss's back to the heap 

            for p in poss:
                heapq.heappush(ts, p)

        return res 