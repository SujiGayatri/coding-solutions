class Solution:
    def isAmicable(self, a, b):
        # code here
        # if a == b:
        #     return False
        def sumDivisors(n):
            total = 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    total += i
                    if i != n // i:
                        total += n // i
            return 0 if n == 1 else total
        return sumDivisors(a) == b and sumDivisors(b) == a