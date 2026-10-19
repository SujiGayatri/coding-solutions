class Solution:
    def sumSqEven(self, n: int) -> int:
        # code here
        sum_squares = 0
        for i in range(1, n + 1):
            even = 2 * i
            sum_squares += even ** 2
        return sum_squares