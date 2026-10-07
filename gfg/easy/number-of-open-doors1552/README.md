# Number Of Open Doors after n Toggles

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Consider a long alley with a  **n** number of doors on one side.

- All the doors are closed initially.
- You move to and fro in the alley changing the states of the doors as follows.
- In the first go, you toggle the states of doors numbered 1, 2, 3,, n.
- In the second go, you toggle the states of doors numbered 2, 4, 6
- In the third go, you alter the states of doors numbered 3, 6, 9
- You continue this till the nth go in which you alter the state of the door numbered n.

You need to find the number of open doors at the end of the procedure.

 **Example :** 

```
Input: n = 2
Output: 1
Explanation: Following the sequence 4 times, we can see that only 1st door will remain open.
```

```
Input: n = 4
Output: 2
Explanation: Following the sequence 4 times, we can see that only 1st and 4th doors will remain open.
```

 **Constraints:** 
1 <= n <= 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T17:32:25.652Z  

```py
class Solution:
    def noOfOpenDoors(self, n):
        # code here
        return math.isqrt(n)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/number-of-open-doors1552/1)