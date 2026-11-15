# Minimum Positive Sum Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums` and  **two**  integers `l` and `r`. Your task is to find the  **minimum**  sum of a  **subarray**  whose size is between `l` and `r` (inclusive) and whose sum is greater than 0.

Return the  **minimum**  sum of such a subarray. If no such subarray exists, return -1.

A  **subarray**  is a contiguous  **non-empty**  sequence of elements within an array.

 

Original
Python3
 **Example 1:** 

 **Input:**  nums = [3, -2, 1, 4], l = 2, r = 3

 **Output:**  1

 **Explanation:** 

The subarrays of length between `l = 2` and `r = 3` where the sum is greater than 0 are:

- [3, -2] with a sum of 1
- [1, 4] with a sum of 5
- [3, -2, 1] with a sum of 2
- [-2, 1, 4] with a sum of 3

Out of these, the subarray `[3, -2]` has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

 **Example 2:** 

 **Input:**  nums = [-2, 2, -3, 1], l = 2, r = 3

 **Output:**  -1

 **Explanation:** 

There is no subarray of length between `l` and `r` that has a sum greater than 0. So, the answer is -1.

 **Example 3:** 

 **Input:**  nums = [1, 2, 3, 4], l = 2, r = 4

 **Output:**  3

 **Explanation:** 

The subarray `[1, 2]` has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 1 <= l <= r <= nums.length
- -1000 <= nums[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 51 ms (beats 40.07%)  
**Memory:** 19.3 MB (beats 64.04%)  
**Submitted:** 2026-11-14T17:19:59.585Z  

```py
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        for i in range(len(nums)):
            total = 0
            for j in range(i, min(i + r, len(nums))):
                total += nums[j]
                length = j - i + 1
                if l <= length <= r and total > 0:
                    min_sum = min(min_sum, total)
        return min_sum if min_sum != float('inf') else -1
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-positive-sum-subarray/)