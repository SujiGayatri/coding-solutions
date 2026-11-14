# BULBLIFE - Rating 846

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Good Quality Bulbs

A bulb company claims that the average lifetime of its bulbs is at least $X$ units.

The company ran a test on $N$ bulbs. You are given the lifetime of $N-1$ of these bulbs. What is the minimum non-negative integer value of lifetime the remaining bulb can have, such that the claim of the company holds true?

### Input Format
- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $X$ - denoting the number of test bulbs and the minimum average lifetime of bulbs in the company's claim.
- The second line of each test case contains $N - 1$ space-separated integers $A_1, A_2, \dots, A_{N-1}$ denoting the lifetimes of $N-1$ of the test bulbs.
### Output Format

For each testcase, output the minimum non-negative integer value of lifetime the remaining bulb can have such that the claim of the company holds true.

### Constraints
- $1 \leq T \leq 100$
- $2 \leq N \leq 100$
- $0 \leq A_i \leq 1000$
- $1 \leq X \leq 1000$
### Sample 1:
Input
Output

```
3
3 4
1 5
4 2
5 8 6
3 1000
0 0

```

```
6
0
3000

```

### Explanation:

Let $Y$ denote the value of the lifetime of the remaining bulb.

 **Test case 1:**  The remaining bulb must have lifetime no less than $6$ units. The average lifetime with $Y = 6$ is $\frac{(1+5+6)}{3} = 4 \geq X$. It can be proven that for any non-negative integer value of $Y \lt 6$ it is not possible to have an average lifeftime of at least $X = 4$.

 **Test case 2:**  The average lifetime with $Y = 0$ is $\frac{(5+8+6+0)}{4} = 4.75 \geq X$. Thus the minimum non negative value which satisfies the condition is $Y = 0$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-14T17:21:43.998Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    required = n * x
    ans = max(0, required - total)
    print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/BULBLIFE)