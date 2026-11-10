class Solution:
    def noOfWays(self, n: int) -> int:
        # code here
        ans = n * n - n + 2
        return ans