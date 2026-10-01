class Solution:
    def isStrong(self, n):
        # code here
        FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        original_num = n
        digit_sum = 0
        while n > 0:
            digit = n % 10
            digit_sum += FACTORIALS[digit]
            n //= 10
        return digit_sum == original_num