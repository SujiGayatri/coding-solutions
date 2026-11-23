# CHSFORMT - Rating 844

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chess Format

Given the time control of a chess match as $a + b$, determine which format of chess out of the given $4$ it belongs to.

$1)$ Bullet if $a + b \lt 3$

$2)$ Blitz if $3 \leq a + b \leq 10$

$3)$ Rapid if $11 \leq a + b \leq 60$

$4)$ Classical if $60 \lt a + b$

### Input Format
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains a single line of input, two integers $a, b$.
### Output Format

For each testcase, output in a single line, answer $1$ for bullet, $2$ for blitz, $3$ for rapid, and $4$ for classical format.

### Constraints
- $1 \leq T \leq 1100$
- $1 \leq a \leq 100$
- $0 \leq b \leq 10$
### Sample 1:
Input
Output

```
4
1 0
4 1
100 0
20 5

```

```
1
2
4
3
```

### Explanation:

 **TestCase $1$:**  Since $a + b = 1 \lt 3$, it belongs to bullet format.

 **TestCase $2$:**  Since $3 \leq (a + b = 5) \leq 10$, it belongs to blitz format.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-23T16:55:11.912Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    s = a + b
    if s < 3:
        print(1)
    elif s <= 10:
        print(2)
    elif s <= 60:
        print(3)
    else:
        print(4)

```

---

[View on CodeChef](https://www.codechef.com/problems/CHSFORMT)