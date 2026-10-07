# FLOW011 - Rating 823

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Gross Salary

In a company an emplopyee is paid as under: If his basic salary is less than Rs. 1500, then HRA = 10% of base salary and DA = 90% of basic salary.
If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the Employee's salary is input, write a program to find his gross salary.

 **NOTE:**  Gross Salary = Basic Salary + HRA + DA

### Input

The first line contains an integer  **T**, total number of testcases. Then follow  **T**  lines, each line contains an integer  **salary**.

### Output

For each test case, output the gross salary of the employee in a new line. Your answer will be considered correct if the absolute error is less than 10-2.

### Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ salary ≤ 100000
### Sample 1:
Input
Output

```
3
1203
10042
1312
```

```
2406.00
20383.16
2624

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T17:34:12.461Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    salary = int(input())
    if salary < 1500:
        hra = 0.10 * salary
        da = 0.90 * salary
    else:
        hra = 500
        da = 0.98 * salary

    gross = salary + hra + da

    print(f"{gross:.2f}")
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW011)