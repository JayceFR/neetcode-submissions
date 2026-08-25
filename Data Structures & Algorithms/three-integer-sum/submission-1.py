class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        '''
        [-4 -1 -1 0 1 2]
        [-1 -1 2]
        [-1  0 1]
        '''
        res = []

        for pos, x in enumerate(nums):
            

            # skips repeats
            if pos > 0 and x == nums[pos-1]:
                continue
            
            # 2sum2 
            lp = pos + 1 
            rp = len(nums) - 1 
            while lp < rp:
                sum = x + nums[lp] + nums[rp]
                if sum > 0:
                    rp -= 1 
                elif sum < 0:
                    lp += 1 
                else:
                    res.append([x, nums[lp], nums[rp]])
                    lp += 1 
                    rp -= 1 
                    while lp < rp and nums[lp] == nums[lp-1]:
                        lp += 1 
        return res 
                    
            
