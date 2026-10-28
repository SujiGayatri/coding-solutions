# PALKINS - Rating 1018

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Palindrome Check

A $1$-indexed array $P$ of length $M$ is called a  *palindrome*  if $P_i = P_{M+1-i}$ holds for each $1 \le i \le M$.
For example, $[2, 2], [3, 1, 3], [4], [12, 12]$ are palindromes whereas $[1, 1, 2]$ and $[12, 21]$ are not.

Chef loves palindromes. Chef also loves the number $K$.

Chef has with him an array $A$ of length $N$.
He can repeatedly modify the array as follows:

- Insert an occurrence of $K$ anywhere into the array. In particular it is allowed to insert before the first element or after the last element.

Is it possible for Chef to perform this modification several times (possibly, zero times) so that the resulting array is a palindrome?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input. The first line of each test case contains two space-separated integers $N$ and $K$ — the length of the array and Chef's favorite number. The second line contains $N$ space-separated integers $A_1, \ldots, A_N$.
### Output Format

For each test case, output on a new line the answer: the string `Yes` if it's possible to obtain a palindrome with several insertions, and the string `No` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. the strings `NO`, `No`, `nO`, and `no` will be treated as equivalent.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \le K, A_i \le 100$
### Sample 1:
Input
Output

```
4
4 3
1 2 3 1
3 5
5 5 5
6 4
1 4 2 1 4 2
5 4
1 4 2 1 4

```

```
Yes
Yes
No
Yes

```

### Explanation:

 **Test case $1$:**  We have $A = [1, 2, 3, 1]$ and $K = 3$.
Insert one occurrence of $K$ between the first two elements to turn the array into $[1, 3, 2, 3, 1]$, which is a palindrome.

 **Test case $2$:**  The array is already a palindrome.

 **Test case $3$:**  It can be shown that no matter how insertions are made, the array will never become a palindrome.

 **Test case $4$:**  We have $A = [1, 4, 2, 1, 4]$ and $K = 4$. One way of forming a palindrome is as follows:

- First, insert one occurrence at the very beginning. The array becomes $[4, 1, 4, 2, 1, 4]$.
- Then, insert one occurrence between the fourth and fifth elements. The array becomes $[4, 1, 4, 2, 4, 1, 4]$ which is a palindrome.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T16:41:04.419Z  

```py
# cook your dish here
t = int(input())

for o in range(t):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    left = 0
    right = N - 1
    possible = True

    while left < right:
        if A[left] == A[right]:
            left += 1
            right -= 1

        elif A[left] == K:
            left += 1

        elif A[right] == K:
            right -= 1

        else:
            possible = False
            break

    print("Yes" if possible else "No")
```

---

[View on CodeChef](https://www.codechef.com/problems/PALKINS)