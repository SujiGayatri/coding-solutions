# Maximum Sum LCM

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive integer  **n**, find the maximum sum of distinct positive integers not exceeding n such that the LCM of all the selected integers is exactly n.

 **Examples:** 

```
Input: n = 2
Output: 3 
Explanation: The distinct numbers you can have are just 1 and 2 and their sum is equal to 3.
```

```
Input: n = 5
Output: 6
Explanation: The distinct numbers you can have are just 1 and 5 and their sum is equal to 6.

```

 **Constraints:** 
1 ≤ n ≤ 10^8

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T17:49:32.296Z  

```py
class Solution:
    def maxSumLCM (self, n):
        # code here 
        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1
        return sum(divisors)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-sum-lcm3025/1)