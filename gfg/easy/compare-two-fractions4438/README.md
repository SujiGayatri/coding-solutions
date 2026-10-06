# Compare two fractions

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a string  **s**  containing two fractions a/b and c/d, compare them and return the  **greater fraction**. If they are equal, then return string " **equal** ".

 **Note** : The string s contains " **a**  **/b, c/d** "(fractions are separated by comma(,) & space()). 

 **Examples :** 

```
Input: s = "5/6, 11/45"
Output: 5/6
Explanation: 5/6 = 0.8333 and 11/45 = 0.2444, So 5/6 is greater fraction.
```

```
Input: s = "8/1, 8/1"
Output: equal
Explanation: We can see that both the fractions are same, so we'll return a string "equal".

```

```
Input: s = "10/17, 9/10"
Output: 9/10
Explanation: 10/17 = 0.588 & 9/10 = 0.9, so the greater fraction is "9/10".
```

 **Constraints:** 
0 ≤ a,c ≤ 103
1 ≤ b,d ≤ 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T16:41:35.436Z  

```py
class Solution:
    def compareFrac(self, s: str) -> str:
        # code here
        f1, f2 = s.split(", ")

        a, b = map(int, f1.split("/"))
        c, d = map(int, f2.split("/"))

        left = a * d
        right = c * b

        if left > right:
            return f1
        elif right > left:
            return f2
        else:
            return "equal"
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/compare-two-fractions4438/1)