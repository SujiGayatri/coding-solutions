# The kth Factor of n

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two positive integers `n` and `k`. A factor of an integer `n` is defined as an integer `i` where `n % i == 0`.

Consider a list of all factors of `n` sorted in  **ascending order**, return  *the* `kth` *factor*  in this list or return `-1` if `n` has less than `k` factors.

 

 **Example 1:** 

```
Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

```

 **Example 2:** 

```
Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.

```

 **Example 3:** 

```
Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

```

 

 **Constraints:** 

- 1 <= k <= n <= 1000

 

 **Follow up:** 

Could you solve this problem in less than O(n) complexity?

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 28.32%)  
**Memory:** 19.3 MB (beats 20.23%)  
**Submitted:** 2026-10-04T16:01:08.366Z  

```py
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        return -1
```

---

[View on LeetCode](https://leetcode.com/problems/the-kth-factor-of-n/)