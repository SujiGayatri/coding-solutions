# N-th Term of GP

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given three integers  **a**,  **r**, and  **n**,

- a is the first term of a Geometric Progression (GP),
- r is the common ratio. 
- n is the position of the term. 

Your task is to calculate the **n-th**  term of the GP. Since the result can be very large, return the answer modulo 1000000007 (i.e. 109+ 7).

 **Examples:** 

```
Input: a = 2, r = 2, n = 4
Output: 16
Explanation: The GP series is 2, 4, 8, 16, 32,... in which 16 is the 4th term.
```

```
Input: a = 4, r = 3, n = 3
Output: 36
Explanation: The GP series is 4, 12, 36, 108,... in which 36 is the 3rd term.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-21T16:01:17.120Z  

```py
class Solution:
	def nthTerm(self, a, r, n):
		# code here
		MOD = 1000000007
        return (a * pow(r, n - 1, MOD)) % MOD
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/series-gp4646/1)