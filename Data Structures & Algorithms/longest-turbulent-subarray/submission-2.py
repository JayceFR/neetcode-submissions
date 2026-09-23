# class Solution:
#     def maxTurbulenceSize(self, arr: List[int]) -> int:
#         if len(arr) == 1:
#             return 1 
#         fp = 0 
#         rp = 1 
#         prev_sign = None 
#         res = rp - fp 
#         while rp < len(arr):
#             sign = arr[rp] > arr[rp-1]
#             if prev_sign is None:
#                 prev_sign = sign   
#             else:
#                 if sign == prev_sign:
#                     # Not turbulent 
#                     fp = rp - 1 
#                     rp -= 1 
#                     prev_sign = None 
#                 else:
#                     prev_sign = sign 
#             res = max(res, rp - fp)
#             rp += 1 
#         return res 

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res