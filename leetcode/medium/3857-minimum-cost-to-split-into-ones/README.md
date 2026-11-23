# Minimum Cost to Split into Ones

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer `n`.

In one operation, you may split an integer `x` into two positive integers `a` and `b` such that `a + b = x`.

The cost of this operation is `a * b`.

Return an integer denoting the  **minimum**  total cost required to split the integer `n` into `n` ones.

 

Original
Python3
 **Example 1:** 

 **Input:**  n = 3

 **Output:**  3

 **Explanation:** 

One optimal set of operations is:

`x`	`a`	`b`	`a + b`	`a * b`	Cost
3	1	2	3	2	2
2	1	1	2	1	1

Thus, the minimum total cost is `2 + 1 = 3`.

 **Example 2:** 

 **Input:**  n = 4

 **Output:**  6

 **Explanation:** 

One optimal set of operations is:

`x`	`a`	`b`	`a + b`	`a * b`	Cost
4	2	2	4	4	4
2	1	1	2	1	1
2	1	1	2	1	1

Thus, the minimum total cost is `4 + 1 + 1 = 6`.

 

 **Constraints:** 

- 1 <= n <= 500

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 56.88%)  
**Memory:** 19.1 MB (beats 88.99%)  
**Submitted:** 2026-11-23T16:52:25.974Z  

```py
class Solution:
    def minCost(self, n: int) -> int:
        return (n * (n - 1)) // 2
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-cost-to-split-into-ones/)