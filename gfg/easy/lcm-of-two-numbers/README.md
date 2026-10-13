# LCM of Two Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two positive integers  **a**  and  **b**, find the Least Common Multiple (LCM) of the two numbers.

 **Examples:** 

```
Input: a = 12, b = 18
Output: 36
Explanation: LCM of 12 and 18 is 36
```

```
Input: a = 5, b = 11
Output: 55
Explanation: LCM of 5 and 11 is 55
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T16:10:18.389Z  

```py
import math
class Solution:
       
    def lcm(self, a, b):
        # code here
        return (a * b) // math.gcd(a, b)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/lcm-of-two-numbers/1)