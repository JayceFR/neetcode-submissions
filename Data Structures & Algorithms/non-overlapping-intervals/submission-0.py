class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # we need to sort and choose if there are any overlaps 
        # then keep the one with the minimum end time and remove the other. 

        intervals.sort()

        res = 0 

        p_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= p_end:
                p_end = end 
            else:
                res += 1 
                p_end = min(end, p_end)

        return res 