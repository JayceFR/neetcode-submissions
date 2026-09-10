class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        quad = []
        def ksum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]: # unique
                        continue
                    quad.append(nums[i])
                    ksum(k-1, i+1, target - nums[i])
                    quad.pop()
            else:
                lp, rp = start, len(nums) - 1 
                while lp < rp:
                    if nums[lp] + nums[rp] < target:
                        lp += 1 
                    elif nums[lp] + nums[rp] > target:
                        rp -= 1
                    else:
                        # found a solution 
                        res.append(quad + [nums[lp], nums[rp]])
                        # keep the unique items the same 
                        lp += 1 
                        while lp < rp and nums[lp] == nums[lp-1]:
                            lp += 1 
        ksum(4, 0, target)
        return res
