# Count Numbers with Digit 4

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a number  **n**, Return the count of total numbers from  **1**  to  **n**  containing  **4** as a digit.

 **Examples:** 

```
Input: n = 9
Output: 1
Explanation: 4 is the only number between 1 to 9 which contains 4 as a digit.
```

```
Input: n = 44
Output: 9
Explanation: 4, 14, 24, 34, 40, 41, 42, 43 & 44, there are total 9 numbers containing 4 as a digit.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T17:04:57.901Z  

```py
class Solution:
    def countNumberswith4(self, n: int) -> int:
        # code here
        count = 0
        for i in range(1, n + 1):
            if '4' in str(i):
                count += 1
        return count
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-numbers-containing-43022/1)