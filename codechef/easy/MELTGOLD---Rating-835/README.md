# MELTGOLD - Rating 835

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Melt Gold

Chef has an ore with melting point of $X$ degrees.
Chef’s kiln has a initial temperature of $Y$ degrees. The temperature of the kiln increases by $i$ degrees after the $i^{th}$ minute.

Find the  **minimum**  time in minutes after which the ore starts melting.

Note:

- We are only concerned about the temperature at the end of each minute and not during a minute.
- The ore starts melting if the temperature of the kiln becomes greater than or equal to the melting point.
### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the melting point of the ore and the initial temperature of kiln.
### Output Format

For each test case, output on a new line, the  **minimum**  time in minutes after which the ore starts melting.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq Y \lt X \leq 10^5$
### Sample 1:
Input
Output

```
3
3 2
5 3
10 5

```

```
1
2
3

```

### Explanation:

 **Test case $1$:**  The initial temperature of the kiln is $2$ and the melting point of ore is $3$.
After first minute, the temperature of kiln increases by $1$.
Thus, after $1$ minute the temperature of kiln becomes $2+1=3$, which is equal to the melting point. Thus, the ore starts melting.

 **Test case $2$:**  The initial temperature of the kiln is $3$ and the melting point of ore is $5$.
After first minute, the temperature of kiln increases by $1$, and becomes $4$.
After second minute, the temperature of kiln increases by $2$, and becomes $6$.

Thus, after $2$ minutes the temperature of kiln becomes $6$, which is greater than the melting point. Thus, the ore starts melting.

 **Test case $3$:**  The initial temperature of the kiln is $5$ and the melting point of ore is $10$.
After first minute, the temperature of kiln increases by $1$, and becomes $6$.
After second minute, the temperature of kiln increases by $2$, and becomes $8$.
After third minute, the temperature of kiln increases by $3$, and becomes $11$.

Thus, after $3$ minutes the temperature of kiln becomes $11$, which is greater than the melting point. Thus, the ore starts melting.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T16:44:45.834Z  

```py
# cook your dish here
import math
t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    diff = X - Y
    t = math.ceil((-1 + math.sqrt(1 + 8 * diff)) / 2)
    print(t)
```

---

[View on CodeChef](https://www.codechef.com/problems/MELTGOLD)