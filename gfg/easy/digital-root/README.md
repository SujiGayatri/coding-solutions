# Digital Root

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a number  **n**. You need to find the **digital root** of n. Digital Root of a number is the recursive sum of its digits until we get a single digit number.

 **Examples :** 

```
Input: n = 1
Output:  1
Explanation: Digital root of 1 is 1
```

```
Input: n = 99999
Output: 9
Explanation: Sum of digits of 99999 is 45 which is not a single digit number, hence sum of digit of 45 is 9 which is a single digit number.
```

 **Constraints:** 
1 ≤ n ≤ 107

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-18T16:18:46.590Z  

```py
class Solution:
    def digitalRoot(self, n: int) -> int:
        # code here
        while n >= 10:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            n = total
        return n
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/digital-root/1)