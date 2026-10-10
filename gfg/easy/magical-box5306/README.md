# Maximum Volume of Cuboid

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integers  **p**  and  **a**, where,

- p represents the perimeter
- a represents the surface area of a cuboid, 

Find the maximum possible volume of the cuboid and return it rounded to 2 decimal places.

 **Note:**  It is guaranteed that a valid cuboid always exists for the given values.

 **Examples:** 

```
Input: p = 22, a = 15
Output: 3.02
Explanation: The maximum attainable volume of the cuboid is 3.02
```

```
Input: p = 20, a = 5
Output: 0.33
Explanation: The maximum attainable volume of the cuboid is 0.33
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T16:42:48.101Z  

```py
import math
class Solution:
    def maxVolume(self, p: int, a: int) -> float:
        # code here
        s = p / 4
        q = a / 2
        d = math.sqrt(s * s - 3 * q)
        t1 = (s + d) / 3
        t2 = (s - d) / 3
        volumes = []
        for t in (t1, t2):
            z = s - 2 * t
            if t > 0 and z > 0:
                volumes.append(t * t * z)
        return round(max(volumes), 2)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/magical-box5306/1)