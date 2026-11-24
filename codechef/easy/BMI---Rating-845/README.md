# BMI - Rating 845

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Body Mass Index

You are given the height $H$ (in metres) and mass $M$ (in kilograms) of Chef. The Body Mass Index (BMI) of a person is computed as $\frac{M}{H^2}$.

Report the category into which Chef falls, based on his BMI:

- Category 1: Underweight if BMI $\leq 18$
- Category 2: Normal weight if BMI $\in \{19$, $20$,$\ldots$, $24\}$
- Category 3: Overweight if BMI $\in \{25$, $26$,$\ldots$, $29\}$
- Category 4: Obesity if BMI $\geq 30$

###Input:

- The first line of input will contain an integer, $T$, which denotes the number of testcases. Then the testcases follow.
- Each testcase contains a single line of input, with two space separated integers, $M, H$, which denote the mass and height of Chef respectively.

###Output: For each testcase, output in a single line, $1, 2, 3$ or $4$, based on the category in which Chef falls.

###Constraints

- $1 \leq T \leq 2*10^4$
- $1 \leq M \leq 10^4$
- $1 \leq H \leq 10^2$
- Its guaranteed that $H^2$ divides $M$.
### Sample 1:
Input
Output

```
3
72 2
80 2
120 2
```

```
1
2
4
```

### Explanation:

 **Case 1:**  Since $\frac{M}{H^2} = \frac{72}{2^2} = 18$, therefore person falls in category $1$.

 **Case 2:**  Since $\frac{M}{H^2} = \frac{80}{2^2} = 20$, therefore person falls in category $2$.

 **Case 3:**  Since $\frac{M}{H^2} = \frac{120}{2^2} = 30$, therefore person falls in category $4$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-24T16:24:40.730Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    m, h = map(int, input().split())
    bmi = m // (h * h)
    if bmi <= 18:
        print(1)
    elif bmi <= 24:
        print(2)
    elif bmi <= 29:
        print(3)
    else:
        print(4)

```

---

[View on CodeChef](https://www.codechef.com/problems/BMI)