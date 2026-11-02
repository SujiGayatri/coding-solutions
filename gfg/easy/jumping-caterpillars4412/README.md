# Jumping Caterpillars

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer m, representing the number of leaves numbered from 1 to m, and an array arr[], where each element represents the jump length of a caterpillar.

- Each caterpillar starts at leaf 1. A caterpillar with jump length k visits the leaves 1, 1 + k, 1 + 2k, 1 + 3k,... until it moves beyond leaf m.
- Whenever a caterpillar visits a leaf, that leaf is considered eaten.

Find the number of leaves that remain uneaten after all caterpillars have completed their jumps.

 **Examples:** 

```
Input: arr[] = [2, 3, 5], m = 10
Output: 2
Explanation: The first caterpillar (jump length = 2) visits the leaves 1, 3, 5, 7, 9. 
The second caterpillar (jump length = 3) visits the leaves 1, 4, 7, 10. 
The third caterpillar (jump length = 5) visits the leaves 1, 6. 
After all caterpillars have completed their jumps, the eaten leaves are 1, 3, 4, 5, 6, 7, 9, and 10, leaving leaves 2 and 8 uneaten. 
Therefore, the number of uneaten leaves is 2.
```

```
Input: arr[] = [2], m = 5 
Output: 2
Explanation: The leaves eaten are 1, 3, 5. The leaves 2,4 are uneaten.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-02T16:26:28.333Z  

```py
class Solution:
    def uneatenLeaves(self, arr: list[int], m: int) -> int:
        # code here
        eaten = [False] * (m + 1)
        for k in set(arr):
            for leaf in range(1, m + 1, k):
                eaten[leaf] = True
        return eaten[1:].count(False)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/jumping-caterpillars4412/1)