# MXSCWN - Rating 843

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Maximum Score

Chef is participating in a tournament.

He must face $N$ opponents.
If he wins against the $i$-th opponent, he will receive $A_i$ coins; whereas if he loses, he will receive $B_i$ coins.
It's guaranteed that $A_i \ge B_i$.

Chef doesn't want to bring too much attention to himself, so he decides that he will  **lose at least once.** 

Under this constraint, what's the maximum total number of coins he can receive?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input. The first line of each test case contains a single integer $N$ — the number of opponents Chef will face. The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$. The third line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.
### Output Format

For each test case, output on a new line the answer: the maximum number of coins Chef can obtain after losing at least once.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \le B_i \le A_i \le 100$
### Sample 1:
Input
Output

```
4
3
5 3 8
3 3 4
1
10
5
4
6 3 8 7
5 1 5 1
4
9 8 7 6
9 8 7 6

```

```
16
5
23
30

```

### Explanation:

 **Test case $1$:**  It's optimal for Chef to win the first match, lose the second match, and win the third match.
This way, he gets $A_1 + B_2 + A_3 = 5+3+8 = 16$ coins.

 **Test case $2$:**  There's only one match, so Chef has no choice but to lose it, receiving $5$ coins.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T17:09:52.743Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    total = sum(A)
    min_loss = min(A[i] - B[i] for i in range(N))
    print(total - min_loss)
```

---

[View on CodeChef](https://www.codechef.com/problems/MXSCWN)