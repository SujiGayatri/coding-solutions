# MIXTURE - Rating 841

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Which Mixture

Chef has $A$ units of solid and $B$ units of liquid. He combines them to create a mixture. What kind of mixture does Chef produce: a solution, a solid, or a liquid?

A mixture is called :

- A solution if $A \gt 0$ and $B \gt 0$,
- A solid if $B = 0$, or
- A liquid if $A = 0$.
### Input Format
- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- Each test case contains two space-separated integers $A$ and $B$ on a single line.
### Output Format

For each test case, output on a single line the type of mixture Chef produces, whether it is a `Solution`, `Solid`, or `Liquid`.  **The output is case sensitive.** 

### Constraints
- $1 \leq T \leq 20$
- $0 \leq A, B \leq 100$
- $A + B \gt 0$
### Subtasks
- Subtask 1 (100 points): Original constraints
### Sample 1:
Input
Output

```
3
10 5
0 3
3 0

```

```
Solution
Liquid
Solid

```

### Explanation:

 **Test case $1$** : Chef adds both solid and liquid to the mixture, hence the mixture is a solution.

 **Test case $2$** : Chef does not add solid to the mixture, hence the mixture is liquid.

 **Test case $3$** : Chef does not add liquid to the mixture, hence the mixture is solid.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-18T16:21:50.363Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    A, B = map(int, input().split())
    if A > 0 and B > 0:
        print("Solution")
    elif B == 0:
        print("Solid")
    else:
        print("Liquid")
```

---

[View on CodeChef](https://www.codechef.com/problems/MIXTURE)