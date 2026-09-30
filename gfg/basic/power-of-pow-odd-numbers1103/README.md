# Sum of Odd Squares

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a single integer  **n**, your task is to find the sum of the square of the first  **n** odd natural Numbers.

 **Examples:** 

```
Input: 2
Output: 10
Explanation: 12 + 32 = 10 
```

```
Input: 3
Output: 35
Explanation: 12 + 32 + 52 = 35  
```

 **Constraints:** 
1 ≤ n ≤ 800

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T16:43:44.329Z  

```py
class Solution:
    def sumofodd(self, n: int) -> int:
        # code here
        result = n * (4 * n * n - 1) // 3
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/power-of-pow-odd-numbers1103/1)