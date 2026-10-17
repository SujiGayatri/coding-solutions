# Count Pairs with Zero XOR

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array  **arr[]**. Find the number of pairs (i, j) such that:

- 0 ≤ i < j < arr.size()
- arr[i] XOR arr[j] = 0

Return the total number of such pairs.

 **Examples:** 

```
Input: arr[] = [1, 3, 4, 1, 4]
Output: 2
Explanation: The pairs at indexes (0, 3) and (2, 4) satisfy arr[i] XOR arr[j] = 0. Therefore, the answer is 2.
```

```
Input: arr[] = [2, 2, 2]
Output: 3
Explanation: The pairs at indexes (0, 1), (0, 2), and (1, 2) satisfy arr[i] XOR arr[j] = 0. Therefore, the answer is 3.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T17:06:11.803Z  

```py
class Solution:
    def countPairs(self, arr):
        # code here
        freq = {}
        count = 0
        for num in arr:
            if num in freq:
                count += freq[num]
            freq[num] = freq.get(num, 0) + 1
        return count
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/counts-zeros-xor-pairs0349/1)