# ADD1234 - Rating 700

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Adding 123 to 4

You have:

- $X$ pieces of papers with $1$ written on it
- $Y$ pieces of paper with $2$ written on it
- $Z$ pieces of paper with $3$ written on it

You want to pair up $2$ pieces of paper such that the sum on each pair adds to $4$. How many such pairs can you make?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains $3$ integers - $X$, $Y$ and $Z$.
### Output Format

For each test case, output on a new line the maximum number of pairs that add to $4$.

### Constraints
- $1 \le T \le 100$
- $1 \le X, Y, Z \le 100$
### Sample 1:
Input
Output

```
2
2 2 1
3 3 3

```

```
2
4

```

### Explanation:

 **Test Case 1**  : You can make the following $2$ pairs:

- One paper with $1$, one paper with $3$
- Two papers with $2$ written.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T17:29:38.677Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    X, Y, Z = map(int, input().split())
    ans = min(X, Z) + Y // 2
    print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/ADD1234)