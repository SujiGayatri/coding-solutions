# Juggler Sequence

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Juggler Sequence is a series of integers in which the first term starts with a positive integer number  *a*  and the remaining terms are generated from the immediate previous term using the below recurrence relation:

Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1.

 **Examples:** 

```
Input: n = 9
Output: 9 27 140 11 36 6 2 1
Explaination: We start with 9 and use 
above formula to get next terms.
```

```
Input: n = 6
Output: 6 2 1
Explaination: 
[61/2] = 2. 
[21/2] = 1.
```

 **Constraints:** 
1 ≤ n ≤ 100

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-28T16:11:19.175Z  

```py
"""
n: int
return: list of int
"""
       
import math 
class Solution:
    def jugglerSequence(self, n):
        # Code here
        res = []

        while True:
            res.append(n)

            if n == 1:
                break

            if n % 2 == 0:
                n = int(math.sqrt(n))
            else:
                n = int(n ** 1.5)
        return res
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/juggler-sequence3930/1)