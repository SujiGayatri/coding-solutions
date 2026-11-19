# Numbers with Odd Factors

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer  **n**, count the numbers having an **odd** number of **factors** from **1 to n**  (inclusive).

 **Examples :** 

```
Input: n = 5
Output: 2
Explanation: The numbers from 1 to 5 with an odd number of factors are 1 and 4.
1 has 1 factor: [1]
4 has 3 factors: [1, 2, 4]
Hence, the count is 2.

```

```
Input: n = 1
Output: 1
Explanation: 1 has exactly one factor, [1], which is odd. Therefore, the count is 1

```

 **Constraints:** 
0 ≤ n ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-19T16:28:08.440Z  

```py
import math
class Solution:
    def count (self, n):
        # code here
        return int(math.sqrt(n))
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-odd-factors0844/1)