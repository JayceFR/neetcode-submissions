class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fp, rp = 0, 0 
        while rp < len(nums):
            if fp == rp and nums[rp] != val:
                fp += 1 
                rp += 1 
            elif nums[rp] == val: 
                rp += 1 
            else:
                nums[fp] = nums[rp]
                fp += 1
                rp += 1 
        print(nums)
        return fp