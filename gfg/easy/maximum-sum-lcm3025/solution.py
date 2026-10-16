class Solution:
    def maxSumLCM (self, n):
        # code here 
        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1
        return sum(divisors)