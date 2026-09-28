class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for x in range(n//2):
            # swap current element with the last one 
            tmp = s[x]
            s[x] = s[n-x-1]
            s[n-x-1] = tmp 