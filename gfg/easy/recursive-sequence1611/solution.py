class Solution:
    def sequence(self, n: int) -> int:
        # code here
        MOD = 10**9 + 7
        total = 0
        start = 1

        for length in range(1, n + 1):
            product = 1

            for j in range(length):
                product = (product * (start + j)) % MOD

            total = (total + product) % MOD
            start += length
        return total