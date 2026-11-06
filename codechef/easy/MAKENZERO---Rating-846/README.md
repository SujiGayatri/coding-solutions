# MAKENZERO - Rating 846

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Make N Zero

You are given a positive integer $N$. In one operation you can:

- Either subtract $3$ or subtract $4$ from $N$.

Can you make $N$ zero by performing any number of operations?

### Input Format
- The first line contains a single integer $T$, denoting the number of test cases.
- The only line of each test case contains a positive integer $N$, denoting the integer which you need to make zero.
### Output Format

For each test case, output `YES` if you can make $N$ zero using any number of operations. Otherwise, print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^4$
### Sample 1:
Input
Output

```
3
1
3
7

```

```
NO
YES
YES

```

### Explanation:

 **Test case $1$:**  You cannot make $N=1$ zero by performing any number of operations.

 **Test case $2$:**  Subtract $3$ from $N=3$ to make it zero in one operation.

 **Test case $3$:**  Subtract $4$ from $N=7$ to make it $N=3$ in one operation. Then, subtract $3$ from $N=3$ to make it zero in second operation.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-06T17:15:23.989Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    if N % 3 == 0 or N % 4 == 0 or N >= 6:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/MAKENZERO)