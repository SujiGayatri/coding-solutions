# DSCPPAS269P - Rating 1000

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Mountain Peak

You are given a list of integers $heights$ representing the heights of $n$ mountain peaks. For each peak, you need to find the height of the next higher peak that comes after it in the list. If there is no higher peak after a given peak, return $-1$ for that peak.

## Function Description
### Function Name:

$next\_higher\_peak$

### Parameters:
- $heights$ : array of heights of mountain peaks.
### Return:

Return an array/list of the next greater height than the current peak.

## Constraints:
- $1 \leq n \leq 100000$
- $0 \leq heights[i] \leq 1000000$

 **The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled automatically.** 

### Input Format
- The first line contains one integer $n$, the size of the list of integers.
- Next line contains $n$ integers $heights[0],heights[1]...heights[n]$, representing the peaks.
### Output Format
- For each peak, print the next higher peak that comes after it in the list. If there is no higher peak for a peak than print $-1$.
### Sample 1:
Input
Output

```
2
1 2
```

```
2 -1
```

### Explanation:

The next greater element for 1 is 2 and for 2 there is no next greater element so for 2 it will be -1.

### Sample 2:
Input
Output

```
4
6 5 3 6
```

```
-1 6 6 -1
```

### Explanation:

For the first 6 there is no element greater than 6 on its right so the peak for the first 6 is -1. For 5, 6 is the next peak as it is on the right side and is greater than 5. For the next element 3, 6 is the peak as it is on the right side and is greater than 3, for the last 6, no peak is there on the right side so -1 is there.

### Sample 3:
Input
Output

```
8
4 7 3 5 2 8 6 9
```

```
7 8 5 8 8 9 9 -1
```

### Explanation:

For 4, the next higher peak is 7. For 7, there are multiple greater elements to the right (8 and 9), but the first greater one is 8. For 3, the next higher peak is 5. For 5, the next higher peak is 8. For 2, the next higher peak is 8. For 8, the next higher peak is 9. For 6, the next higher peak is 9. For 9, there is no higher peak to the right, so -1.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-22T17:06:20.842Z  

```py
def next_higher_peak(heights):
    # Write your code here
    n = len(heights)
    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= heights[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(heights[i])

    return result
```

---

[View on CodeChef](https://www.codechef.com/problems/DSCPPAS269P)