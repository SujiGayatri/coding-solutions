# Divisibility by 8

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string  **s**  representing a non-negative decimal number, determine whether the number is divisible by 8. Return  **true** if it is divisible by  **8**, otherwise return  **false**.

 **Examples:** 

```
Input: s = "16"
Output: true
Explanation:
The given number is divisible by 8. So the answer is true.

```

```
Input: s = "54141111648421214584416464555"
Output: false
Explanation:
Given Number is not divisible by 8. So the answer for this is false.

```

 **Constraints:** 
1 ≤ |s| ≤ 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T17:15:39.673Z  

```py
class Solution:
    def isDivBy8(self, s):
        # code here
        num = 0
        for ch in s:
            num = (num * 10 + int(ch)) % 8
        return num == 0
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-if-a-number-is-divisible-by-83957/1)