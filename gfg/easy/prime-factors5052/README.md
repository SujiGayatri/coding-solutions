# Unique Prime Factors in Sorted Order

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a number  **n**. Find its unique prime factors in increasing order.

 **Examples:** 

```
Input: n = 100
Output: [2, 5]
Explanation: Unique prime factors of 100 are 2 and 5.

```

```
Input: n = 60
Output: [2, 3, 5]
Explanation: Prime factors of 60 are 2, 2, 3, 5. Unique prime factors are 2, 3 and 5.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-22T17:06:13.442Z  

```py
class Solution:
    def primeFac(self, n: int) -> list[int]:
        # code here
        factors = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.append(n)
        return factors
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/prime-factors5052/1)