# P4HOME - Rating 749

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Close Friends

Chef lives at position $x$ on the $x$ - axis.

Chef has $2y$ friends, each living at every integer point in the range: [$x$ − $y$, $x$ + $y$] except the position $x$ itself.

Chef wants to visit his friends, but his mother has placed a strict rule: Chef is allowed to travel at most $z$ units away from his home in either direction. This means Chef can only move within the interval [$x$ − $z$, $x$ + $z$].

Your task is to determine how many of Chef’s friends live within the range Chef is allowed to travel.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input. The line contains three space-separated integers $x$, $y$, and $z$ — denoting Chef’s position on the $x$-axis, the friend range $[x - y, x + y]$, and the maximum distance Chef is allowed to travel.
### Output Format

For each test case, output a single integer — the number of friends Chef can visit.

### Constraints
- $1 \leq T \leq 3⋅10^5$
- $-50 \leq x \leq 50$
- $0 \leq y, z \leq 50$
### Sample 1:
Input
Output

```
4
0 2 1
10 3 5
-5 4 2
7 10 0

```

```
2
6
4
0

```

### Explanation:
- In the 1st test case, chef's friends live at position [-2, 2] except 0 and chef can visit positions [-1, 1]. So he can visit 2 friends.
- In the 4th test case, chef can only visit position 7. So he cannot travel to any of his friends.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-04T15:58:22.912Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    ans = 2 * min(y, z)
    print(ans)

```

---

[View on CodeChef](https://www.codechef.com/problems/P4HOME)