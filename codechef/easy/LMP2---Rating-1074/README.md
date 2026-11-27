# LMP2 - Rating 1074

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Odd String

You are given a string $S$ of length $N$ consisting only of lowercase English letters.

A string is called an  **odd string**  if and only if:

- For every pair of indices $i < j$ such that $S_i = S_j$, the distance between them is odd, i.e. $(j - i)$ is odd.
- In other words, no two equal characters are allowed to appear at an even distance from each other.

You are allowed to rearrange the characters of the string $S$ in any order.

Determine whether it is possible to rearrange $S$ such that it becomes an odd string.

### Input Format
- The first line contains an integer $T$ — the number of test cases.
- For each test case: The first line contains a single integer $N$ — the length of the string. The next line contains a string $S$ consisting consisting of lowercase English letters.
### Output Format

For each test case, output `YES` if it is possible to rearrange $S$ into an odd string, otherwise output `NO`.

Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings `NO`, `no`, `No`, and `nO` will all be treated as equivalent.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 100$
- $S$ consists of lowercase English letters only
### Sample 1:
Input
Output

```
8
1
a
2
bb
5
xxxxx
7
aabccbd
8
aabccbdc
8
abcdabcd
8
codechef
5
abcde

```

```
YES
YES
NO
YES
NO
YES
YES
YES

```

### Explanation:
- For the first test case, a is already an odd string. So, no rearrangement is needed.
- For the second test case, bb is already an odd string. b occurs at two indices $1$ and $2$. We can see that $2-1 = 1$ is odd.
- For the third test case, xxxxx remains unchanged however we rearrange. Now x occurs at indices $1$ and $3$. Since $3-1 = 2$ is even, it is impossible to create an odd string.
- For the fourth test case, aabccbd is already an odd string.
- For the sixth test case, abcdabcd can be rearranged to aabbccdd which is an odd string.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T17:02:21.769Z  

```py
# cook your dish here
from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    freq = Counter(s)

    if max(freq.values()) > 2:
        print("NO")
    else:
        print("YES")
```

---

[View on CodeChef](https://www.codechef.com/problems/LMP2)