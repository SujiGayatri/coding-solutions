class Solution:   
    def waysToBreakNumber(self, n: int) -> int:
        # code here
        MOD = 10**9 + 7
        return ((n + 1) * (n + 2) // 2) % MOD