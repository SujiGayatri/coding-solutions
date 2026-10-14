# Ways to Break into 3 Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a number  **n**, break it into 3 whole numbers such that they sum up to the original number and find the number of ways to do so. Since this number can be very large, return it modulo 109+7. 

 **Examples:** 

```
Input: n = 2
Output: 6
Explanation: Possible ways to break the number:
0 + 0 + 2 = 2 
0 + 2 + 0 = 2
2 + 0 + 0 = 2
0 + 1 + 1 = 2
1 + 1 + 0 = 2
1 + 0 + 1 = 2

```

```
Input: n = 3
Output: 10
Explanation: Possible ways to break the number:
0 + 0 + 3 = 3
0 + 3 + 0 = 3
3 + 0 + 0 = 3
0 + 1 + 2 = 3
0 + 2 + 1 = 3
1 + 0 + 2 = 3
1 + 2 + 0 = 3
2 + 0 + 1 = 3
2 + 1 + 0 = 3
1 + 1 + 1 = 3
```

 **Constraints:** 
1 ≤ n ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T16:39:50.463Z  

```py
class Solution:   
    def waysToBreakNumber(self, n: int) -> int:
        # code here
        MOD = 10**9 + 7
        return ((n + 1) * (n + 2) // 2) % MOD
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/break-a-number5913/1)