class Solution:
    def fib (self,n):
        #code here
        a, b = 0, 1
        for i in range(n):
            a, b = b, (a + b) % 10
        return a