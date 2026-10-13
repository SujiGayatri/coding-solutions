# FLOW014 - Rating 838

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Grade The Steel

A certain type of steel is graded according to the following conditions.

- Hardness of the steel must be greater than 50
- Carbon content of the steel must be less than 0.7
- Tensile strength must be greater than 5600

The grades awarded are as follows:

- Grade is 10 if all three conditions are met
- Grade is 9 if conditions (1) and (2) are met
- Grade is 8 if conditions (2) and (3) are met
- Grade is 7 if conditions (1) and (3) are met
- Grade is 6 if only one condition is met
- Grade is 5 if none of the three conditions are met

Write a program to display the grade of the steel, based on the values of hardness, carbon content and tensile strength of the steel, given by the user.

### Input Format

The first line contains an integer  **T**, total number of testcases. Then follow  **T**  lines, each line contains three numbers  **hardness**,  **carbon content**  and  **tensile strength**  of the steel.

### Output Format

For each test case, print Grade of the steel depending on Conditions, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 0 ≤ hardness, carbon content, tensile strength ≤ 10000
### Sample 1:
Input
Output

```
3 
53 0.6 5602
45 0 4500
0 0 0 

```

```
10
6
6

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T16:11:41.109Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    hardness, carbon, tensile = map(float, input().split())
    c1 = hardness > 50
    c2 = carbon < 0.7
    c3 = tensile > 5600
    if c1 and c2 and c3:
        grade = 10
    elif c1 and c2:
        grade = 9
    elif c2 and c3:
        grade = 8
    elif c1 and c3:
        grade = 7
    elif c1 or c2 or c3:
        grade = 6
    else:
        grade = 5

    print(grade)
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW014)