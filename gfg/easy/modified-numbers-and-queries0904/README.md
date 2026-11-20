# Range Sum of Distinct Prime Factors

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given q queries, where each query gives a pair (l, r), find the sum of all distinct prime factors of every number in the range [l, r], for each query.

 **Note:**  Count each prime factor only once for each number. For example, 6 has distinct prime factors 2 and 3, so its corresponding value is 5. Similarly, 12 has distinct prime factors 2 and 3, so its corresponding value is also 5.

 **Examples:** 

```
Input: l[] = [1, 2, 3, 4], r[] = [5, 6, 7, 8]
Output: [12, 17, 22, 21]
Explanation:
Query 1: range [1,5] -> 0+2+3+2+5 = 12
Query 2: range [2,6] -> 2+3+2+5+5 = 17
Query 3: range [3,7] -> 3+2+5+5+7 = 22
Query 4: range [4,8] -> 2+5+5+7+2 = 21
```

```
Input: l[] = [1], r[] = [6]
Output: [17]
Explanation:
1 has 0 prime factors, so sum is 0
2 has 2 only, so sum is 2
3 has 3 only, so sum is 3
4 has 2 only, so sum is 2
5 has 5 only, so sum is 5
6 has 2 and 3 only, so sum is 2 + 3 = 5
Overall sum = 0 + 2 + 3 + 2 + 5 + 5 = 17.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-20T17:20:45.419Z  

```py
class Solution:
    def getSum(self, l: list[int], r: list[int]) -> list[int]:
        # code here
        n = max(r)
        arr = [0] * (n + 1)
        for p in range(2, n + 1):
            if arr[p] == 0:
                for j in range(p, n + 1, p):
                    arr[j] += p
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + arr[i]
        ans = []
        for i in range(len(l)):
            ans.append(prefix[r[i]] - prefix[l[i] - 1])
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/modified-numbers-and-queries0904/1)