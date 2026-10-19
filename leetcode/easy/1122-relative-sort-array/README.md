# Relative Sort Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`. Elements that do not appear in `arr2` should be placed at the end of `arr1` in  **ascending**  order.

 

 **Example 1:** 

```
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

```

 **Example 2:** 

```
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]

```

 

 **Constraints:** 

- 1 <= arr1.length, arr2.length <= 1000
- 0 <= arr1[i], arr2[i] <= 1000
- All the elements of arr2 are distinct.
- Each arr2[i] is in arr1.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 49.84%)  
**Memory:** 19.2 MB (beats 82.95%)  
**Submitted:** 2026-10-18T16:57:15.824Z  

```py
class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        result = []
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]
        for num in sorted(count):
            result.extend([num] * count[num])
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/relative-sort-array/)