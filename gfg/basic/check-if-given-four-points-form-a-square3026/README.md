# Check if  Four Points Form a Square

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an 2D array points[] which represents coordinates of four points in a plane. Find if the four points can form a square or not. Return true if they form a square else return false.

 **Examples :** 

```
Input: points[] = [[0, 0], [0, 1], [1, 0], [1, 1]]
Output: true
Explanation: These points form a square which can be clearly seen in the below image.

```

```
Input: points[] = [[0, 0], [1, 1], [1, 0], [0, 2]]
Output: false
Explanation: These four points do not form a square.

```

 **Constraints:** 
0 ≤ X-coordinate, Y-coordinate ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T15:48:17.989Z  

```py
class Solution:
    def isSquare(self, points):    
        #code here
        def dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        distances = []
        for i in range(4):
           for j in range(i + 1, 4):
               distances.append(dist(points[i], points[j]))

        distances.sort()
        return (
               distances[0] > 0 and
               distances[0] == distances[1] == distances[2] == distances[3] and
               distances[4] == distances[5] and
               distances[4] == 2 * distances[0]
           )
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-if-given-four-points-form-a-square3026/1)