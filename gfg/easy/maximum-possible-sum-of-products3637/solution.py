class Solution:
    def maxProductSum(self, a, b):
        # code here
        a.sort()
        b.sort()
        total = 0
        for i in range(len(a)):
            total += a[i] * b[i]
        return total