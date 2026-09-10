class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # get all partitions and thenxor them
        if not nums:
            return 0
        def partitions(sp) -> List[List[int]]:
            if sp == len(nums) - 1:
                return [[nums[sp]]]
            restStuff = partitions(sp + 1)
            res = []
            for part in restStuff:
                res.append([nums[sp]] + part)
                res.append(part)
            res.append([nums[sp]])
            return res 
        partition = partitions(0)
        sum = 0 
        for part in partition:
            xors = 0
            for num in part:
                xors ^= num 
            sum += xors 
        return sum
