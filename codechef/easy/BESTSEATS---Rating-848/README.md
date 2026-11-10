# BESTSEATS - Rating 848

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Best Seats

Chef and Chefina are trying to watch a cricket game. They have already decided a row of $N$ seats where they will seat, but they are yet to figure out the exact $2$ seats they will buy.

The $i$-th seat in the row costs $A_i$ coins to buy. Obviously, they have to sit next to each other, so they will only buy adjacent seats.

Can you figure out the minimum cost for them to buy $2$ seats such that they are able to sit together?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains a single integer $N$ - the number of seats in the row. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the minimum cost of buying $2$ adjacent seats.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $1 \le A_i \le 100$
### Sample 1:
Input
Output

```
3
2
5 10
3
1 3 2
5
100 98 97 99 97

```

```
15
4
195
```

### Explanation:

 **Test Case 1**  : There are only $2$ seats in the row, so they have to buy those $2$. They cost a total of $5 + 10$ coins.

 **Test Case 2**  : They can choose to buy seat numbered $1$ and seat numbered $2$ for a cost of $1 + 3 = 4$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-10T17:14:39.150Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = float('inf')
    for i in range(n - 1):
        ans = min(ans, arr[i] + arr[i + 1])
    print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/BESTSEATS)