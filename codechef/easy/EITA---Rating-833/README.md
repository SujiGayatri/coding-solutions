# EITA - Rating 833

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Maximum Production

Chefland has $7$ days in a week. Chef is very conscious about his work done during the week.

There are two ways he can spend his energy during the week. The first way is to do $x$ units of work every day and the second way is to do $y$ ($\gt x$) units of work for the first $d$ ($\lt 7$) days and to do $z$ ($\lt x$) units of work thereafter since he will get tired of working more in the initial few days.

Find the maximum amount of work he can do during the week if he is free to choose either of the two strategies.

### Input
- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, four integers $d$, $x$, $y$, $z$.
### Output

For each testcase, output in a single line the answer to the problem.

### Constraints
- $1 \leq T \leq 5\cdot 10^3$
- $1 \leq d \lt 7$
- $1 \leq z \lt x \lt y \leq 18$
### Subtasks

 **Subtask #1 (100 points):**  Original constraints

### Sample 1:
Input
Output

```
3
1 2 3 1
6 2 3 1
1 2 8 1
```

```
14
19
14
```

### Explanation:

 **Test Case $1$:**  Using the first strategy, Chef does $2 \cdot 7 = 14$ units of work and using the second strategy Chef does $3 \cdot 1 + 1 \cdot 6 = 9$ units of work. So the maximum amount of work that Chef can do is $\max(14, 9) = 14$ units by using the first strategy.

 **Test Case $2$:**  Using the first strategy, Chef does $2 \cdot 7 = 14$ units of work and using the second strategy Chef does $3 \cdot 6 + 1 \cdot 1 = 19$ units of work. So the maximum amount of work that Chef can do is $\max(14, 19) = 19$ units by using the second strategy.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T17:51:07.069Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    d, x, y, z = map(int, input().split())
    strategy1 = 7 * x
    strategy2 = d * y + (7 - d) * z
    print(max(strategy1, strategy2))
```

---

[View on CodeChef](https://www.codechef.com/problems/EITA)