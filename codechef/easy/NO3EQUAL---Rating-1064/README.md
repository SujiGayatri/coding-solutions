# NO3EQUAL - Rating 1064

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### No 3 Equal

You have a string $S$ of length $N$ consisting of lower case English characters.

You say that a string is good if there is  **no**  index $i$ such that $1 \le i \le N - 2$ and $S_i = S_{i + 1} = S_{i + 2}$.

Find the minimum number of edits you need to make to the string to make it good. Each edit is changing one character to any other lower case English character.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains an integer $N$. The second line contains a string $S$.
### Output Format

For each test case, output the minimum edits.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $|S| = N$
- $S$ contains lowercase English Characters.
### Sample 1:
Input
Output

```
3
6
aaaaaa
4
aabc
5
baaac

```

```
2
0
1

```

### Explanation:

 **Test Case 1** : We can change to $aabaab$ which is good.

 **Test case 2**  : The string is good already.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-21T16:03:38.689Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    count = 0
    i = 0

    while i < n - 2:
        if s[i] == s[i + 1] == s[i + 2]:
            count += 1
            i += 3
        else:
            i += 1

    print(count)
```

---

[View on CodeChef](https://www.codechef.com/problems/NO3EQUAL)