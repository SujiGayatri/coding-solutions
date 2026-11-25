# VISA - Rating 857

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chefland Visa

Ash is trying to get visa to Chefland. For the visa to be approved, he needs to satisfy the following three criteria:

- Solve at least $x_1$ problems on Codechef.
- Have at least $y_1$ current rating on Codechef.
- Make his last submission at most $z_1$ months ago.

You are given the number of problems solved by Chef ($x_2$), his current rating ($y_2$) and the information that he made his last submission $z_2$ months ago. Determine whether he will get the visa.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains six space-separated integers $x_1$, $x_2$, $y_1$, $y_2$, $z_1$ and $z_2$.
### Output

For each test case, print a single line containing the string `"YES"` if Chef will get the visa or `"NO"` if he will not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq T \leq 5,000$
- $20 \leq x_1, x_2 \leq 50$
- $1,900 \leq y_1, y_2 \leq 2,100$
- $1 \leq z_1, z_2 \leq 6$
### Sample 1:
Input
Output

```
4
20 50 2100 1900 6 6
50 20 1900 1900 5 5
20 20 1900 1900 1 6
27 27 1920 1920 3 3
```

```
NO
NO
NO
YES
```

### Explanation:

 **Example case 1:**  Chef's rating is less than the minimum required rating.

 **Example case 2:**  Chef has solved a smaller number of problems than the minimum required number.

 **Example case 3:**  Chef's last submission was made before the allowed period.

 **Example case 4:**  All three conditions are met.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-25T17:03:11.137Z  

```py
# cook your dish here
T = int(input())
for i in range(T):
    x1, x2, y1, y2, z1, z2 = map(int, input().split())

    if x2 >= x1 and y2 >= y1 and z2 <= z1:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/VISA)