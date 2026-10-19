# Repeated Integer Division by 2

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two integers  **n**  and  **m**, halve n exactly m - 1 times using integer division. Return the resulting value.

 **Examples:** 

```
Input: n = 100, m = 4
Output: 12
Explanation: The sequence of numbers is 100, 50, 25, 12.
```

```
Input: n = 10, m = 5
Output: 0
Explanation: The sequence is 10, 5, 2, 1 and 0.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T17:08:54.823Z  

```py
class Solution:
    def mthHalf(self, n: int, m: int) -> int:
        # code here
        for _ in range(m - 1):
            n //= 2
        return n
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/geek-and-coffee-shop5721/1)