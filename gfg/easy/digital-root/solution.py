class Solution:
    def digitalRoot(self, n: int) -> int:
        # code here
        while n >= 10:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            n = total
        return n