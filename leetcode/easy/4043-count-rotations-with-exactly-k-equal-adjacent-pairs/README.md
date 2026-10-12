# Count Rotations With Exactly K Equal Adjacent Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a string `s` of length `n` and an integer `k`.

A  **cyclic rotation**  of `s` is obtained by choosing a prefix of `s` whose length is between 0 and `n - 1` (inclusive), and moving it to the end of the string while preserving the order of all characters.

For  **every**  cyclic rotation of `s`, let its  **score**  be the number of indices `i` such that `0 <= i < n - 1` and the characters at positions `i` and `i + 1` are equal.

Return the number of cyclic rotations of `s` whose score equals `k`.

 

 **Example 1:** 

 **Input:**  s = "aab", k = 1

 **Output:**  2

 **Explanation:** 

The cyclic rotations of `s` are:

- "aab": The characters at positions 0 and 1 are equal, so score = 1.
- "aba": No two adjacent characters are equal, so score = 0.
- "baa": The characters at positions 1 and 2 are equal, so score = 1.

Since `score` equals `k` for 2 cyclic rotations of `s`, the answer is 2.

 **Example 2:** 

 **Input:**  s = "abca", k = 0

 **Output:**  1

 **Explanation:** 

The cyclic rotations of `s` are:

- "abca": No two adjacent characters are equal, so score = 0.
- "bcaa": The characters at positions 2 and 3 are equal, so score = 1.
- "caab": The characters at positions 1 and 2 are equal, so score = 1.
- "aabc": The characters at positions 0 and 1 are equal, so score = 1.

Since `score` equals `k` for only 1 cyclic rotation of `s`, the answer is 1.

 

 **Constraints:** 

- 2 <= n == s.length <= 100
- s only consists of lowercase English letters.
- 0 <= k <= n - 1

## Solution

**Language:** Python  
**Runtime:** 71 ms (beats 34.12%)  
**Memory:** 19.2 MB (beats 92.46%)  
**Submitted:** 2026-10-12T17:19:37.999Z  

```py
class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        for shift in range(n):
            rotated = s[shift:] + s[:shift]
            score = 0
            for i in range(n - 1):
                if rotated[i] == rotated[i + 1]:
                    score += 1
            if score == k:
                count += 1
        return count
```

---

[View on LeetCode](https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/)