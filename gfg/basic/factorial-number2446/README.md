# Factorials in Array

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array  **arr[]**  containing  **n**  integers, return a list containing all elements from the array that are factorial numbers of some positive integer.

- If a factorial appears multiple times, include all occurrences in the output.
- Preserve the original order.

 **Examples :** 

```
Input: arr[] = [2, 1, 5, 9]
Output: [2, 1]
Explanation: 
2 is the factorial of 2, i.e. 2! = 1 * 2 = 2
1 is the factorial of 1, i.e. 1! = 1
```

```
Input: arr[] = [2, 5, 3, 6, 9, 12, 24]
Output: [2, 6, 24] 
Explanation:
2 is the factorial of 2, i.e. 2! = 1 x 2 = 2 
6 is the factorial of 3, i.e. 3! = 1 × 2 × 3 = 6
24 is the factorial of 4, i.e. 4! = 1 × 2 × 3 × 4 = 24
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T16:38:13.304Z  

```py
class Solution:
    def factorialNumbers(self, arr):
        # code here
        factorials = set()
        fact = 1
        i = 1
        while fact <= 10**9:
            factorials.add(fact)
            i += 1
            fact *= i
        result = [x for x in arr if x in factorials]
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/factorial-number2446/1)