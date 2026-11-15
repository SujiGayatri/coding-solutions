# FLOW008 - Rating 776

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Helping Chef

Write a program, which takes an integer  **N**  and if the number is less than 10 then display "Thanks for helping Chef!" otherwise print "-1".

### Input Format

The first line contains an integer  **T**, total number of testcases. Then follow  **T**  lines, each line contains an integer  **N**.

### Output Format

For each test case, output the given string or -1 depending on conditions, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- -20 ≤ N ≤ 20
### Sample 1:
Input
Output

```
3 
1
12
-5

```

```
Thanks for helping Chef!
-1
Thanks for helping Chef!

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-15T16:54:09.417Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    if n < 10:
        print("Thanks for helping Chef!")
    else:
        print(-1)
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW008)