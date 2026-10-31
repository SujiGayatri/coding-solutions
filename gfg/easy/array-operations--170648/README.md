# Make Array 0 with Subarray Operations

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array  **arr[]**  of integers, find the minimum number of operations required to make all its elements 0.

In one operation,

- Choose a contiguous subarray containing only non-zero elements and replace all its elements with 0.
- The operation can be performed only if the array contains at least one 0.

**Examples:
**

```
Input: arr[] = [3, 0, 4, 5] 
Output: 2
Explanation: There are two contiguous groups of non-zero elements: [3] and [4, 5]. Each group can be replaced with 0 in one operation.
```

```
Input: arr[] = [10, 4, 9, 6, 10, 10, 4, 4] 
Output: -1 
Explanation: The array does not contain 0, so no operation can be performed.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T17:08:05.790Z  

```py
class Solution:
    def arrayOperations(self, arr: list[int]) -> int:
        # code here 
        if 0 not in arr:
            return -1
        operations = 0
        in_group = False
        for x in arr:
            if x != 0:
                if not in_group:
                    operations += 1
                    in_group = True
            else:
                in_group = False
        return operations
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/array-operations--170648/1)