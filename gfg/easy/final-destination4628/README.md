# Check if Destination Reachable with x Moves

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given three integers  **a**,  **b**, and  **x**, where (a, b) represents a target position on an infinite 2D plane and x represents the exact number of moves available.

- A robot starts at (0, 0) and in one move can travel one unit left, right, up, or down.
- Find whether the robot can reach the position (a, b) in exactly x moves. Return true if possible; otherwise, return false.

 **Examples:** 

```
Input: a = 5, b = 5, x = 11
Output: false
Explanation:The minimum number of moves required to reach (5, 5) is |5| + |5| = 10. One extra move remains, which is odd, so the robot cannot reach the destination in exactly 11 moves.
```

```
Input: a = 0, b = 0, x = 2
Output: true
Explanation: The robot can move one step away from the origin and return in the next step. Therefore, it can be at (0, 0) after exactly 2 moves.

```

 **Constraints:** 
-108 <= a,b <= 108
1 <= x <= 2*108

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-30T17:05:56.410Z  

```py
class Solution:
    def canReach(self, a, b, x):
        # code here
        min_moves = abs(a) + abs(b)
        return x >= min_moves and (x - min_moves) % 2 == 0
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/final-destination4628/1)