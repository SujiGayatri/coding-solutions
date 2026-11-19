# DSAAGP384 - Rating 1050

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Duplicate Integers

Given $N$ non-negative integers, check if there is any duplicate value present.

## Function Declaration
### Function Name

$hasDuplicate$ – This function checks whether the given array contains any duplicate elements.

### Parameters
- $nums$ : An integer array containing $N$ elements.
### Return Value
- Returns $true$ if at least one duplicate element exists in the array.
- Returns $false$ if all elements are distinct.
## Constraints:
- $1 \leq T \le 800$
- All integers are non-negative and don't exceed $100$

 **The input and output formats given below are only if you want to test using custom inputs.** 

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input: The first line of each test case contains a positive integer $N$ - the number of integers. The second line of each test case contains $N$ space separated integers.
### Output Format

For each test case, output on a new line:

- YES if input integers have duplicates in it.
- NO if all integers are unique.
### Sample 1:
Input
Output

```
2
4
1 2 3 4
5
1 2 3 1 2
```

```
NO
YES
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-19T16:30:30.389Z  

```py
def has_duplicate(nums):
    # write your code here 
    return len(nums) != len(set(nums))
```

---

[View on CodeChef](https://www.codechef.com/problems/DSAAGP384)