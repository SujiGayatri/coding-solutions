# Find Lucky Integer in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of integers `arr`, a  **lucky integer**  is an integer that has a frequency in the array equal to its value.

Return  *the largest  **lucky integer**  in the array*. If there is no  **lucky integer**  return `-1`.

 

 **Example 1:** 

```
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

```

 **Example 2:** 

```
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

```

 **Example 3:** 

```
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

```

 

 **Constraints:** 

- 1 <= arr.length <= 500
- 1 <= arr[i] <= 500

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 70.21%)  
**Submitted:** 2026-10-05T16:10:34.846Z  

```py
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        frequency = {}
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        lucky = -1
        for num, count in frequency.items():
            if num == count:
                lucky = max(lucky, num)
        return lucky
```

---

[View on LeetCode](https://leetcode.com/problems/find-lucky-integer-in-an-array/)