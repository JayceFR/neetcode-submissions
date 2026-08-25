class Solution:
    def trap(self, height: List[int]) -> int:

        leftMaxs = [0]
        currMax = 0 
        for x in range(len(height) - 1):
            currMax = max(currMax, height[x])
            leftMaxs.append(currMax)

        # right maxs 
        rightMaxs = [0]
        currMax = 0 
        for x in range(len(height)-1, 0, -1):
            currMax = max(currMax, height[x])
            rightMaxs.insert(0, currMax)
        water = 0 
        for pos, h in enumerate(height):
            water += max(0, min(leftMaxs[pos], rightMaxs[pos]) - h)
        return water 

        
        

        '''
        [0 2 0 3 1 0 1 3 2 1]

        [0 2 2 ].
        need to have either 
        where a > 0
        a <a >=a 
        >=a <a a 
        [2 0 1]
        [1 0 2]
        [3 1 2] is valid too
        we need to maximise the number of times we have a little number between >=a and a
        so [3 1 1 1 1 1 2] optimal or even [3 0 0 0 0 0 0 2] 
        '''