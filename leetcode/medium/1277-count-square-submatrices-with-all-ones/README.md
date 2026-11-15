# Count Square Submatrices with All Ones

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a `m * n` matrix of ones and zeros, return how many  **square**  submatrices have all ones.

 

Original
Python3
 **Example 1:** 

```
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

```

 **Example 2:** 

```
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

```

 

 **Constraints:** 

- 1 <= arr.length <= 300
- 1 <= arr[0].length <= 300
- 0 <= arr[i][j] <= 1

## Solution

**Language:** Python  
**Runtime:** 62 ms (beats 24.38%)  
**Memory:** 22.7 MB (beats 31.93%)  
**Submitted:** 2026-11-15T16:51:55.155Z  

```py
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(
                            dp[i-1][j],
                            dp[i][j-1],
                            dp[i-1][j-1]
                        )
                    total += dp[i][j]
        return total
```

---

[View on LeetCode](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)