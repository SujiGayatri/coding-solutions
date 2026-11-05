# K Sized Subarray with Minimum Average

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array  **arr[]**  and an integer  **k**, find the contiguous subarray of size  **k**  that has the minimum average value among all possible subarrays of size k. Return position (or index + 1) of the first element of that subarray.

 **Examples :** 

```
Input: arr[] = [30, 20, 10], k = 1
Output: 3
Explanation: Subarrays of length 1 are {30}, {20}, {10}. {10} has the least average equal to 10.

```

```
Input: arr[] = [30, 20, 10], k = 2
Output: 2
Explanation: Subarrays of length 2 are {30, 20}, {20, 10}. {20, 10} has the least average equal to (20 + 10)/2 = 15.
```

 **Constraints:** 
1 ≤ k ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-05T16:26:15.980Z  

```py
class Solution:
    def leastAvg(self, arr, k):
        # code here
        n = len(arr)
        window_sum = sum(arr[:k])
        min_sum = window_sum
        ans = 0
        for i in range(k, n):
            window_sum += arr[i] - arr[i-k]
            if window_sum < min_sum:
                min_sum = window_sum
                ans = i - k + 1
        return ans + 1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/subarray-with-least-average5031/1)