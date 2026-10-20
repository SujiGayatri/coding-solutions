class Solution:
    def sumofproduct(self, n: int) -> int:
        # code here
        total = 0
        for x in range(1, n + 1):
            y = n // x
            total += x * y
        return total