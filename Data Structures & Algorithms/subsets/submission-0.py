class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        current = nums[0]
        subs = self.subsets(nums[1:])
        new  = []

        for s in subs:
            n = [current]
            for el in s:
                n.append(el)
            new.append(n)
        return new + subs 
        
        