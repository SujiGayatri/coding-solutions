# Greatest English Letter in Upper and Lower Case

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string of English letters `s`, return  *the  **greatest** English letter which occurs as  **both**  a lowercase and uppercase letter in*  `s`. The returned letter should be in  **uppercase**. If no such letter exists, return  *an empty string*.

An English letter `b` is  **greater**  than another letter `a` if `b` appears  **after**  `a` in the English alphabet.

 

 **Example 1:** 

```
Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.

```

 **Example 2:** 

```
Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

```

 **Example 3:** 

```
Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case.

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s consists of lowercase and uppercase English letters.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 20.71%)  
**Submitted:** 2026-10-09T17:14:45.299Z  

```py
class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = set(s)
        for ch in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if ch in letters and ch.lower() in letters:
                return ch
        return ""
```

---

[View on LeetCode](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/)