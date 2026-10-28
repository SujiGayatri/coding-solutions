class Solution:
    def factorialNumbers(self, arr):
        # code here
        factorials = set()
        fact = 1
        i = 1
        while fact <= 10**9:
            factorials.add(fact)
            i += 1
            fact *= i
        result = [x for x in arr if x in factorials]
        return result