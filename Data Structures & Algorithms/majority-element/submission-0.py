class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        res = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            if curr == res: 
                count += 1 
            elif count > 0:
                count -= 1 
            else:
                count += 1 
                res = curr 
        
        return res 