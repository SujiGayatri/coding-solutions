class Solution:
    def sumofodd(self, n: int) -> int:
        # code here
        result = n * (4 * n * n - 1) // 3
        return result