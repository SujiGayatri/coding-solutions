# Largest Combination With Bitwise AND Greater Than Zero

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The  **bitwise AND**  of an array `nums` is the bitwise AND of all integers in `nums`.

- For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
- Also, for nums = [7], the bitwise AND is 7.

You are given an array of positive integers `candidates`. Compute the  **bitwise AND**  for all possible  **combinations**  of elements in the `candidates` array.

Return  *the size of the  **largest**  combination of* `candidates` *with a bitwise AND  **greater**  than* `0`.

 

Original
Python3
 **Example 1:** 

```
Input: candidates = [16,17,71,62,12,24,14]
Output: 4
Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

```

 **Example 2:** 

```
Input: candidates = [8,8]
Output: 2
Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.

```

 

 **Constraints:** 

- 1 <= candidates.length <= 105
- 1 <= candidates[i] <= 107

## Solution

**Language:** Python  
**Runtime:** 447 ms (beats 79.82%)  
**Memory:** 27.7 MB (beats 92.35%)  
**Submitted:** 2026-11-17T17:06:05.268Z  

```py
class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        ans = 0
        for i in range(24):
            count = 0
            for num in candidates:
                if num & (1 << i):
                    count += 1
            ans = max(ans, count)
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/)