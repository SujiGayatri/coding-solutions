# Ways to Color Balls

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given `n` balls arranged in a line, each ball must be colored either  **RED**  or  **BLUE**. A coloring is considered valid if the number of adjacent positions where the color changes (from RED to BLUE or BLUE to RED) is at most `2`. Find the total number of valid ways to color all the balls.

 **Examples:** 

```
Input: n = 1
Output: 2
Explanation: Possible ways to color are {{R}, {B}}. So the answer is 2.
```

```
Input: n = 2
Output: 4
Explanation: Possible ways to color are {{RB},{BR},{RR},{BB}}. So the answer is 4.
```

 **Constraints:** 
1 ≤ n ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-10T17:13:07.105Z  

```py
class Solution:
    def noOfWays(self, n: int) -> int:
        # code here
        ans = n * n - n + 2
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/ball-coloring3450/1)