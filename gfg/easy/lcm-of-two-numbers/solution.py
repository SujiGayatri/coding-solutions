import math
class Solution:
       
    def lcm(self, a, b):
        # code here
        return (a * b) // math.gcd(a, b)