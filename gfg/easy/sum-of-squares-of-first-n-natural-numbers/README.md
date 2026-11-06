# Sum of Squares of  n Natural

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer  **n.**  The task is to calculate the sum of the squares of the first   **n**  natural numbers.

 **Examples:** 

```
Input: n = 2
Output: 5
Explanation: 12 + 22 = 5
```

```
Input: n = 3
Output: 14
Explanation: 12 + 22 + 32 = 14
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-06T17:14:20.873Z  

```py
class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, n):
        # code here
        return n * (n + 1) * (2 * n + 1) // 6
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-of-squares-of-first-n-natural-numbers/1)