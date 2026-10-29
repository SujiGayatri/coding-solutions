# Area of Triangle

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given three sides of a triangle  **a**,  **b**  and  **c**  in the form of integers. Find the area of the triangle. The triangle may not exist. In such cases, the area is 0.
 **Note:**  Output the area up to 3 decimal places without rounding off.

 **Examples:** 

```
Input: a = 2, b = 2, c = 3
Output: 1.984
Explanation: The triangle with sides 2, 2, and 3 has an area of 1.984313... square units. Since we don't round off, this becomes 1.984.
```

```
Input: a = 1, b = 3, c = 1
Output: 0.000
Explanation: No triangle can be formed with sides 1, 3, and 1 (since 1 + 1 < 3), so the area is 0.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T16:26:16.100Z  

```py
class Solution:
    def findArea(self, a, b, c):
        # code here
        if a + b <= c or a + c <= b or b + c <= a:
            return 0.000
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        area = int(area * 1000) / 1000
        return area
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/area-of-a-triangle5739/1)