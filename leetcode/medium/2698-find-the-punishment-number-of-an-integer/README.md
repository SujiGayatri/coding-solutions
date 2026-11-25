# Find the Punishment Number of an Integer

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a positive integer `n`, return  *the  **punishment number***  of `n`.

The  **punishment number**  of `n` is defined as the sum of the squares of all integers `i` such that:

- 1 <= i <= n
- The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.

 

Original
Python3
 **Example 1:** 

```
Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182

```

 **Example 2:** 

```
Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478

```

 

 **Constraints:** 

- 1 <= n <= 1000

## Solution

**Language:** Python  
**Runtime:** 613 ms (beats 59.70%)  
**Memory:** 19.1 MB (beats 85.07%)  
**Submitted:** 2026-11-25T16:58:57.382Z  

```py
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(s, target):
            if not s:
                return target == 0
            for j in range(len(s)):
                num = int(s[:j+1])
                if num <= target and canPartition(s[j+1:], target - num):
                    return True

            return False

        total = 0

        for i in range(1, n + 1):
            square = i * i
            if canPartition(str(square), i):
                total += square

        return total
```

---

[View on LeetCode](https://leetcode.com/problems/find-the-punishment-number-of-an-integer/)