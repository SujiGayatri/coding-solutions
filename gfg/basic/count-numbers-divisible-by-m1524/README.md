# Divisible by M in a Range

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two numbers a and b which define a range, where a ≤ b. Find the count of total numbers in the given range [a … b] divisible by m **.** 

 **Examples:** 

```
Input: a = 6, b = 15, m = 3
Output: 4 
Explanation: 6, 9, 12, 15 are divisible by 3. Hence answer is 4.

```

```
Input: a = 25, b = 100, m = 30
Output: 3
Explanation: 30, 60, 90 are divisible by 30. Hence answer is 3.
```

 **Constraints:** 
1 ≤ a, b, m ≤ 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T15:48:51.760Z  

```py
class Solution:
    def countDivisibles(self, a, b, m):
        # Code Here
        return b // m - (a - 1) // m
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-numbers-divisible-by-m1524/1)