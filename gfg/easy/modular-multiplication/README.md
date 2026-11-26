# Modular Multiplication

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given three integers  **a**,  **b**, and  **M**, perform modular multiplication and return  **(a × b) % M**, where **%**  denotes the  **modulo**  operation.

 **Examples:** 

```
Input: a = 5, b = 3, M = 11
Output: 4
Explanation: a × b = 5 × 3 = 15, 15 % 11 = 4, so the result is 4.
```

```
Input: a = 12, b = 15, M = 7
Output: 5
Explanation: a × b = 12 × 15 = 180, 180 % 7 = 5, so the result is 5.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-26T16:47:28.134Z  

```py
class Solution:
    def modmul(self, a, b, M):
        # code here
        result = (a * b) % M
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/modular-multiplication/1)