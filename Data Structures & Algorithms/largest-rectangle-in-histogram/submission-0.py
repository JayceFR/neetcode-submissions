class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hmap = {}
        maxArea = 0 
        for h in heights:
            
            for k in hmap.keys():
                if k > h:
                    #need to reset 
                    maxArea = max(maxArea, hmap[k] * k)
                    hmap[k] = 0 
            
            for x in range(1, h+1):
                hmap[x] = hmap.get(x, 0) + 1 
        
        for k,v in hmap.items():
            maxArea = max(maxArea, k * v)
        
        return maxArea 