# BID - Rating 833

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Pep Bidding

Pep is known for his golden bids on football matches. Surprisingly, he has a rather simple strategy!

Team $A$ and team $P$ are playing against each other, and each of them have $N$ players.
For each $i$ from $1$ to $N$,

- Pep believes that the $i$-th player on team $A$ has an attack power of $attA_i$, and a defense power of $defA_i$.
- Similarly, the $i$-th player on team $P$ has an attack power of $attP_i$, and a defense power of $defP_i$.

The total attack power of a team is the sum of the attack powers of all of its $N$ players.
The total defense power is defined similarly.

If the total attack power of one team is  **strictly**  greater than the total attack power of the other team,  *and*  its total defense power is  **strictly**  greater than the total defense power of the other team, Pep bids for that team.
Otherwise, he'll bid for a draw.

Can you tell what Pep will bid on?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of five lines of input. The first line of each test case contains a single integer $N$, the number of players on both teams. The second line contains $N$ space-separated integers $attA_1, attA_2, \ldots, attA_N$ — the elements of $attA$. The third line contains $N$ space-separated integers $defA_1, defA_2, \ldots, defA_N$ — the elements of $defA$. The fourth line contains $N$ space-separated integers $attP_1, attP_2, \ldots, attP_N$ — the elements of $attP$. The fifth line contains $N$ space-separated integers $defP_1, defP_2, \ldots, defP_N$ — the elements of $defP$.
### Output Format

For each test case, output on a new line a string representing what Pep bids for: either `"A"`, `"P"`, or `"DRAW"` (without quotes).

Each letter of the output may be printed in either lowercase or uppercase, i.e, the strings `DRAW`, `draw`, `dRaW`, and so on will be considered equivalent.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 2000$
- $0 \leq attA_i \leq 1000$
- $0 \leq defA_i \leq 1000$
- $0 \leq attP_i \leq 1000$
- $0 \leq defP_i \leq 1000$
- The sum of $N$ over all test cases won't exceed $2000$.
### Sample 1:
Input
Output

```
3
3
17 9 10
2 1 6
8 16 7
6 2 0
2
100 1
10 0
0 0
5 5
1
1
2
3
4
```

```
A
DRAW
P
```

### Explanation:

 **Test case $1$:** 

- Total attack power of team $A$ = $17 + 9 + 10 = 36$
- Total defense power of team $A$ = $2 + 1 + 6 = 9$
- Total attack power of team $P$ = $8 + 16 + 7 = 31$
- Total defense power of team $P$ = $6 + 2 + 0 = 8$ Since team $A$ dominates in both attack and defense, Pep bids for team $A$.

 **Test case $2$:** 

- Total attack power of team $A = 101$
- Total defense power of team $A = 10$
- Total attack power of team $P = 0$
- Total defense power of team $P = 10$

Though team $A$ dominates $P$ in the attack department, there is no dominance in defense department (note that Pep requires the value to be  *strictly*  greater).
Hence, Pep bids for a draw.

 **Test case $3$:** 

- Total attack power of team $A = 1$
- Total defense power of team $A = 2$
- Total attack power of team $P = 3$
- Total defense power of team $P = 4$ Since team $P$ dominates in both attack and defense, Pep bids for team $P$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T17:05:54.553Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    attA = list(map(int, input().split()))
    defA = list(map(int, input().split()))
    attP = list(map(int, input().split()))
    defP = list(map(int, input().split()))
    total_att_A = sum(attA)
    total_def_A = sum(defA)
    total_att_P = sum(attP)
    total_def_P = sum(defP)

    if total_att_A > total_att_P and total_def_A > total_def_P:
        print("A")
    elif total_att_P > total_att_A and total_def_P > total_def_A:
        print("P")
    else:
        print("DRAW")
```

---

[View on CodeChef](https://www.codechef.com/problems/BID)