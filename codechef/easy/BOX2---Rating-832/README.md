# BOX2 - Rating 832

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### 2 Boxes

You have $2$ boxes, the first having $X$ stones, and the second having $Y$ stones.

You want the (absolute) difference between the stones of the $2$ boxes to be exactly $K$.

Each second, you can take a stone from the $1^{st}$ box and put it in the $2^{nd}$, or take from the $2^{nd}$ and put it in the $1^{st}$ box.

Find the minimum time till the difference between the stones of the $2$ boxes becomes exactly $K$. If it is impossible, print $-1$ instead.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first and only line of input contains $3$ integers - $X, Y$ and $K$.
### Output Format

For each test case, output on a new line the minimum time to get the difference to exactly $K$ or $-1$ if impossible.

### Constraints
- $1 \le T \le 10^3$
- $1 \le X, Y \le 10$
- $0 \le K \le X + Y$
### Sample 1:
Input
Output

```
7
2 2 0
2 2 1
2 2 4
2 2 2
8 3 1
4 8 2
4 8 3

```

```
0
-1
2
1
2
1
-1

```

### Explanation:

 **Test Case 1**  : The difference is already $0$.

 **Test Case 2**  : It can be shown that it is impossible.

 **Test case 3**  : We can spend $2$ seconds, taking one stone from $1^{st}$ box to $2^{nd}$ each time. So, we will have $0$ stones in $1^{st}$ box and $4$ stones in $2^{nd}$ box after $2$ seconds. The difference is exactly $4$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T15:50:43.185Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    X, Y, K = map(int, input().split())
    diff = abs(X - Y)
    if diff == K:
        print(0)
    elif abs(diff - K) % 2 == 0:
        print(abs(diff - K) // 2)
    else:
        print(-1)
```

---

[View on CodeChef](https://www.codechef.com/problems/BOX2)