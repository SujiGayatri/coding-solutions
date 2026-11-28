"""
n: int
return: list of int
"""
       
import math 
class Solution:
    def jugglerSequence(self, n):
        # Code here
        res = []

        while True:
            res.append(n)

            if n == 1:
                break

            if n % 2 == 0:
                n = int(math.sqrt(n))
            else:
                n = int(n ** 1.5)
        return res