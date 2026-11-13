class Solution:
    def countNonDivisible(self, n):
        # code here
        limit = 2520
        count = 0
        for i in range(1, limit + 1):
            if __import__('math').gcd(i, limit) == 1:
                count += 1
        q, rem = divmod(n, limit)
        ans = q * count
        for i in range(1, rem + 1):
            if __import__('math').gcd(i, limit) == 1:
                ans += 1

        return ans