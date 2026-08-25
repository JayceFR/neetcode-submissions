class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2 
        poSums = {0}
        for x in nums:
            for y in poSums.copy():
                z = x + y
                if (z == target):
                    return True
                poSums.add(z)
        return False 