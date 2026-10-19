# Sum of n Even Squares

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a single integer  **n**, your task is to find the sum of the square of the first n even natural Numbers. 

 **Examples:** 

```
Input: n = 2
Output: 20
Explanation: 22 + 42 = 20

```

```
Input: n = 3
Output: 56
Explanation: 22 + 42 + 62 = 56 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-18T16:57:10.190Z  

```py
class Solution:
    def sumSqEven(self, n: int) -> int:
        # code here
        sum_squares = 0
        for i in range(1, n + 1):
            even = 2 * i
            sum_squares += even ** 2
        return sum_squares
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/power-of-pow-even-number5440/1)