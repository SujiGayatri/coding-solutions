class Solution:
    def sumMatrix(self, n: int, q: int) -> int:
        # code here
        low = max(1, q - n)
        high = min(n, q - 1)
        if low > high:
            return 0
        return high - low + 1