# Status of Doors after n Toggles

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

There are  **n** closed doors and  **n**  people.

- All doors are initially closed
- Person i toggles the status of every ith door, i.e., doors whose number is a multiple of i. 
- Every person does the above step (step 2)  from person 1 to n.

Find the final status of all doors after all persons have acted once.

 **Examples:** 

```
Input: n = 3
Output: 1 0 0 
Explanation: Initial status of rooms (0 0 0). Person 1 changes to (1 1 1). Person 2 changes to (1 0 1). Person 3 changes to (1 0 0).
```

```
Input: n = 2
Output: 1 0
Explanation: Initial status of rooms (0 0). Person 1 changes to (1, 1) and person 2 changes to (1, 0)
```

 **Constraints:** 
1 ≤ n ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T16:52:27.759Z  

```py
class Solution:
    def checkDoorStatus(self, n: int) -> list[int]:
       # Code here
        result = []
        for door in range(1, n + 1):
            root = int(door ** 0.5)
            if root * root == door:
                result.append(1)
            else:
                result.append(0)
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-if-the-door-is-open-or-closed2013/1)