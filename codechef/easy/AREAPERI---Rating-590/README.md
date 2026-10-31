# AREAPERI - Rating 590

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Area OR Perimeter

Write a program to obtain length $(L)$ and breadth $(B)$ of a rectangle and check whether its area is greater or perimeter is greater or both are equal.

### Input Format
- First line will contain the length $(L)$ of the rectangle.
- Second line will contain the breadth $(B)$ of the rectangle.
### Output Format

Output 2 lines.

In the first line print "Area" if area is greater otherwise print "Peri" and if they are equal print "Eq".(Without quotes).

In the second line print the calculated area or perimeter (whichever is greater or anyone if it is equal).

### Constraints
- $1 \leq L \leq 1000$
- $1 \leq B \leq 1000$
### Sample 1:
Input
Output

```
1
2

```

```
Peri
6

```

### Explanation:

Area = 1 * 2 = 2
Peri = 2 * (1 + 2) = 6
Since Perimeter is greater than Area, hence the output is :
Peri
6

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T17:09:39.853Z  

```py
# cook your dish here
L = int(input())
B = int(input())
area = L * B
perimeter = 2 * (L + B)
if area > perimeter:
    print("Area")
    print(area)
elif perimeter > area:
    print("Peri")
    print(perimeter)
else:
    print("Eq")
    print(area)
```

---

[View on CodeChef](https://www.codechef.com/problems/AREAPERI)