from math import gcd,isqrt
from functools import reduce
class Solution:
    def sameMod(self, arr):
        # code here
        g = 0

        for i in range(1, len(arr)):
            g = gcd(g, abs(arr[i] - arr[0]))
        if g == 0:
            return -1
        count = 0
        for i in range(1, isqrt(g) + 1):
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1
        return count