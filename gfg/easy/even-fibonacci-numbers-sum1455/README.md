# Even Fibonacci Numbers Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a number  **n**  find the  **sum**  of all the even valued terms in the Fibonacci sequence less than or equal to n.
The first few terms of Fibonacci Numbers are, 1, 1,  **2**, 3, 5,  **8**, 13, 21,  **34**, 55, 89,  **144**, 233,… (Even numbers are highlighted).

 **Examples :** 

```
Input: n = 8
Output: 10
Explanation: There are two even fibonacci numbers less than equal to 8, 8 and 2 so sum is 8 + 2 = 10.
```

```
Input: n = 89
Output: 44
Explanation:There are three even fibonacci numbers less than equal to 89, 8, 2 and 34 so sum is 8 + 2 + 34 = 44. 
```

 **Constraints:** 
1 ≤ n ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-09T16:19:44.015Z  

```py
class Solution:
    def evenFibSum(self, n: int) -> int:
        # code here
        a, b = 1, 1
        total = 0
        while a <= n:
            if a % 2 == 0:
                total += a
            a, b = b, a + b
        return total
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/even-fibonacci-numbers-sum1455/1)