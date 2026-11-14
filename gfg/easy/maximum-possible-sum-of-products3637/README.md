# Max Sum of Products from Two Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two arrays **a[]**  and  **b[]**  of size  **n**  containing positive integers. Rearrange the elements of both arrays so that the value of: a[0]  *b[0] + a[1]*  b[1] +... + a[n-1] * b[n-1] becomes maximum. Each element of a[] and b[] must be used exactly once.

 **Examples:** 

```
Input: a[] = [1, 2, 3], b[] = [4, 5, 1]
Output: 24
Explanation: After rearranging: a[] = [1, 2, 3] and b[] = [1, 4, 5]. Maximum sum = (1  *1) + (2*  4) + (3 * 5) = 1 + 8 + 15 = 24.

```

```
Input: a[] = [3, 1, 1], b[] = [6, 5, 4]
Output: 27
Explanation: After rearranging: a[] = [1, 1, 3] and b[] = [4, 5, 6]. Maximum sum = (1  *4) + (1*  5) + (3 * 6) = 4 + 5 + 18 = 27.

```

 **Constraints:** 

1 ≤ n ≤ 103
1 ≤ ai, bi ≤ 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-14T17:20:49.498Z  

```py
class Solution:
    def maxProductSum(self, a, b):
        # code here
        a.sort()
        b.sort()
        total = 0
        for i in range(len(a)):
            total += a[i] * b[i]
        return total
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-possible-sum-of-products3637/1)