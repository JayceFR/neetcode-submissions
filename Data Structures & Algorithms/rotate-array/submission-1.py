class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)

        def reverse(start: int, end: int):
            fp = start 
            lp = end 
            while fp < lp:
                tmp = nums[fp]
                nums[fp] = nums[lp]
                nums[lp] = tmp 
                fp += 1 
                lp -= 1 
        
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
        