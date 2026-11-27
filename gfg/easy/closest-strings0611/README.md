# Two Words Minimum Distance

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a list of words  **s**  and two specific words  **word1**  and  **word2**, find the minimum distance between the indices of word1 and word2 in the list.

The distance between two words is defined as the absolute difference between their indices.

 **Note:** 

- word1 and word2 may occur multiple times in the list.
- If either word1 or word2 is not present in the list, return -1.
- If both words are present, return the minimum possible distance between any occurrence of word1 and any occurrence of word2.

 **Example :** 

```
Input: s = [ "the", "quick", "brown", "fox", "quick"], word1 = "the", word2 = "fox"
Output: 3
Explanation: Minimum distance between the words "the" and "fox" is 3

```

```
Input: s = ["geeks", "for", "geeks", "contribute", "practice"], word1 = "geeks", word2 = "practice"
Output: 2
Explanation: Minimum distance between the words "geeks" and "practice" is 2
```

```
Input: s = ["geeks", "for", "geeks", "contribute", "practice"], word1 = "hello", word2 = "practice"
Output: -1
Explanation: The word "hello" is not present in the list, so return -1.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T17:02:13.830Z  

```py
class Solution:
    def shortestDistance(self, s: list[str], word1: str, word2: str) -> int:
        # code here
        i1 = -1
        i2 = -1
        ans = float('inf')

        for i in range(len(s)):
            if s[i] == word1:
                i1 = i

            if s[i] == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1 - i2))

        if ans == float('inf'):
            return -1

        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/closest-strings0611/1)