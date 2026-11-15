# Amicable Pair

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integers  **a**  and  **b**, find if they form an amicable pair.

Two distinct numbers are called amicable numbers if:

- The sum of all proper divisors of a is equal to b, and
- The sum of all proper divisors of b is equal to a.

A proper divisor of a number is a positive divisor other than the number itself.

 **Examples:** 

```
Input: a = 220, b = 284
Output: true 
Explanation: Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, whose sum is 284.
Proper divisors of 284 are 1, 2, 4, 71, 142, whose sum is 220.
Therefore, 220 and 284 form an amicable pair.
```

```
Input: a = 10, b = 20
Output: false
Explanation: The sum of the proper divisors of 10 is 1 + 2 + 5 = 8, which is not equal to 20.
Therefore, 10 and 20 do not form an amicable pair.
```

 **Constraints:** 
1 ≤ a, b ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-15T16:46:51.234Z  

```py
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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/amicable-pair0804/1)