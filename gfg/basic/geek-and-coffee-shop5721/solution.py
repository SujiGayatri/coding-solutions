class Solution:
    def mthHalf(self, n: int, m: int) -> int:
        # code here
        for _ in range(m - 1):
            n //= 2
        return n