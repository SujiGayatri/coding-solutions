# SUMREDUCTION - Rating 1027

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Sum Reduction

You are given an array $A$ of $N$ elements.

In one operation, you may choose two distinct indices $i$ and $j$ such that the bitwise AND of $A_i$ and $A_j$ is $0$, i.e. $A_i \& A_j = 0$.

Then, remove both $A_i$ and $A_j$ from the array, and insert their sum $A_i + A_j$ back into the array.

Determine whether it is possible to reduce the array to exactly one element after performing a finite number of operations.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input. The first line of each test case contains a single integer $N$, denoting the size of the array. The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$, denoting the elements of the array.
### Output Format

For each test case, output `Yes` if the array can be reduced to exactly one element, otherwise output `No`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $0 \leq A_i \lt 2^{30}$
### Sample 1:
Input
Output

```
4
2
3 4
3
1 2 3
1
7
4
69 24 128 34

```

```
Yes
No
Yes
Yes

```

### Explanation:
- Test Case $1$: Since $3 \& 4 = 0$, we can merge them into $3 + 4 = 7$. The array is reduced to one element, so the answer is Yes.
- Test Case $2$: It can be shown that no finite sequence of operations can reduce the array to a single element. Hence, the answer is No.
- Test Case $3$: The array already contains exactly one element, so the answer is Yes.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-20T17:21:41.038Z  

```py
# cook your dish here
t = int(input())
for u in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    while len(a) > 1:
        found = False

        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if (a[i] & a[j]) == 0:
                    s = a[i] + a[j]

                    a.pop(j)
                    a.pop(i)
                    a.append(s)

                    found = True
                    break

            if found:
                break

        if not found:
            break

    print("Yes" if len(a) == 1 else "No")
```

---

[View on CodeChef](https://www.codechef.com/problems/SUMREDUCTION)