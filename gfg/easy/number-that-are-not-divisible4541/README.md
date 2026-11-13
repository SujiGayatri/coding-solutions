# Count Numbers Not Divisible by 2–10

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive integer  **n**, how many integers in the range  **[1, n]**  are not divisible by any of the numbers from  **2**  to  **10**.

 **Examples:** 

```
Input: n = 11
Output: 2
Explanation: The numbers are 1 and 11.
```

```
Input: n = 2
Output: 1
Explanation: The only number is 1.
```

```
Input: n = 30
Output: 7
Explanation: The numbers are 1, 11, 13, 17, 19, 23 and 29
```

 **Constraints:** 
1 ≤ n ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-13T16:34:27.090Z  

```py
class Solution:
    def countNonDivisible(self, n):
        # code here
        limit = 2520
        count = 0
        for i in range(1, limit + 1):
            if __import__('math').gcd(i, limit) == 1:
                count += 1
        q, rem = divmod(n, limit)
        ans = q * count
        for i in range(1, rem + 1):
            if __import__('math').gcd(i, limit) == 1:
                ans += 1

        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/number-that-are-not-divisible4541/1)