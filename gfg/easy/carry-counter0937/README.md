# Addition Carry Counter

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two non-negative integers  **s1**  and  **s2**  as strings, count the number of carry operations that occur while adding them digit by digit.

Return the  **total**  number of carries generated during the addition of  **s1**  and  **s2**.

 **Examples:** 

```
Input: s1 = "34", s2 = "25"
Output: 0
Explanation:
There are no carries when s1 and s2 are added.
```

```
Input: s1 = "4634", s2 = "1757"
Output: 2
Explanation:
There are 2 carries when s1 and s2 are added.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-17T17:07:26.330Z  

```py
class Solution:
    def getCarries(self, s1, s2):
        # code here
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        count = 0
        while i >= 0 or j >= 0:
            d1 = int(s1[i]) if i >= 0 else 0
            d2 = int(s2[j]) if j >= 0 else 0
            total = d1 + d2 + carry
            if total >= 10:
                count += 1
                carry = 1
            else:
                carry = 0
            i -= 1
            j -= 1
        return count
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/carry-counter0937/1)