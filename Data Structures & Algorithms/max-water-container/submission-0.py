class Solution:
    def maxArea(self, heights: List[int]) -> int:
        fp = 0 
        rp = len(heights) - 1 
        area = 0 
        while fp < rp :
            area = max(area, min(heights[fp], heights[rp]) * (rp - fp))
            if heights[fp] < heights[rp]:
                fp += 1 
            else:
                rp -= 1 
        return area