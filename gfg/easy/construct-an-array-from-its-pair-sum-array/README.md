# Construct an array from its pair-sum array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a  **pair-sum**  array  **arr[]**  return the  **original**  array  **res[]**. A pair-sum array for an array is the array that contains  **sum of all pairs**  in ordered form, i.e., arr[0] is sum of res[0] and res[1], arr[1] is sum of res[0] and res[2] and so on.

 **Note:**  If the size of original array  **res[]**  is  **n**, then the size of pair-sum array  **arr[]** would be  **n * (n -1) /2**. We may assume that the  **pair-sum array**  arr[] is appropriate in size.
Note that, if the original array is correct then the driver code will print  **true**, else  **false** ;

 **Examples:** 

```
Input: arr[] = [4, 5, 3]
Output: true
Explanation: A valid original array is [3, 1, 2], pairwise sums are (3 + 1), (3 + 2) and (1 + 2).
```

```
Input: arr[] = [3]
Output: true
Explanation: One of the valid original array is [1, 2].
```

**Constraints: 
**1 ≤ n ≤ 103
1 ≤ arr[i] ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-11T17:16:28.768Z  

```py
class Solution:
    def constructArr(self, arr):
        # code here
        m = len(arr)
        if m == 1:
            return [1, arr[0] - 1]
        n = int((1 + (1 + 8 * m) ** 0.5) / 2)
        res = [0] * n
        res[0] = (arr[0] + arr[1] - arr[n - 1]) // 2
        res[1] = arr[0] - res[0]
        for i in range(2, n):
            res[i] = arr[i - 1] - res[0]
        return res
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/construct-an-array-from-its-pair-sum-array/1)