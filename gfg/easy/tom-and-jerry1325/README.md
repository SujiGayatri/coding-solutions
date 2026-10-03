# Tom and Jerry

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer  **n**, Tom and Jerry play a game. On each turn, a player chooses a divisor of the current value of n that is less than n and subtracts it from n.

The resulting value becomes the n for the next turn. A player who has no valid divisor to subtract loses the game. Tom makes the first move, and both players play optimally. 

Return true if Tom wins; otherwise, return false.

 **Note:**  When n = 1, there is no divisor less than n, so the player whose turn it is, loses.

 **Examples:** 

```
Input: n = 2
Output: true
Explanation: Tom subtracts 1 from 2, making n = 1. Jerry has no valid move, so Tom wins.
```

```
Input: n = 3
Output: false
Explanation: Tom can only subtract 1 from 3, making n = 2. Jerry then subtracts 1 from 2, making n = 1. Tom has no valid move, so Tom loses.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T15:37:50.397Z  

```py
class Solution:
    def numsGame(self, n: int) -> bool:
        # code here 
        return n % 2 == 0
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/tom-and-jerry1325/1)