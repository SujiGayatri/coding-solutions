# DSACPR66 - Rating 650

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Find smallest and largest numbers

Given an array of integers, your task is to find the  **smallest (minimum)**  and  **largest (maximum)**  elements present in the array.

## Function Declaration
### Function Name

$findMinMax$ – This function scans the array to determine both the minimum and maximum values.

### Parameters
- $n$ : An integer representing the number of elements in the array.
- $arr$ : A list/array of $n$ integers.
### Return Value
- Returns a pair/list/array containing exactly two integers: the first element should be the smallest value, and the second element should be the largest value.
## Constraints
- $1 \le n \le 10^5$
- $-10^9 \le arr[i] \le 10^9$

 *The input and output formats provided below are only for testing with custom inputs. You only need to complete the core logic function.* 

### Input Format
- The first line contains an integer $n$, representing the size of the array.
- The second line contains $n$ space-separated integers, representing the elements of the array.
### Output Format
- Print the smallest and largest elements in the array on a single line, separated by a space.
### Sample 1:
Input
Output

```
10
4 3 53 13 2 44 55 35 56 34
```

```
2 56
```

### Explanation:

In the given array [4 3 53 13 2 44 55 35 56 34]:
The smallest element is $2$.
The largest element is $56$.
Therefore, the output is 2 56.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T16:55:38.487Z  

```py
def findMinMax(n: int, arr: list[int]) -> list[int]:
    minimum = arr[0]
    maximum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return [minimum, maximum]
```

---

[View on CodeChef](https://www.codechef.com/problems/DSACPR66)