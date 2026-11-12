class Solution:
    def sumOfDivisors(self, N):
    	#code here 
    	total = 0

        for i in range(1, N + 1):
            if N % i == 0:
                for j in range(1, i + 1):
                    if i % j == 0:
                        total += j
        return total