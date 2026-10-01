# Strong Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A Strong Number is a number whose value is equal to the sum of the factorials of its digits.

Given a positive integer  **n**, find if it is a Strong Number.

 **Examples:** 

```
Input: 145
Output: true
Explanation: The sum of the factorials of its digits is: 1! + 4! + 5! = 1 + 24 + 120 = 145.
Since the sum equals the original number, 145 is a Strong Number.

```

```
Input: 5314
Output: false
Explanation: The sum of the factorials of its digits is not equal to 5314. Therefore, it is not a Strong Number.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T16:35:51.896Z  

```py
class Solution:
    def isStrong(self, n):
        # code here
        FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        original_num = n
        digit_sum = 0
        while n > 0:
            digit = n % 10
            digit_sum += FACTORIALS[digit]
            n //= 10
        return digit_sum == original_num
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/strong-numbers4336/1)