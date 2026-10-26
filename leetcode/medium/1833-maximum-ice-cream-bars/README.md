# Maximum Ice Cream Bars

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are `n` ice cream bars. You are given an array `costs` of length `n`, where `costs[i]` is the price of the `ith` ice cream bar in coins. The boy initially has `coins` coins to spend, and he wants to buy as many ice cream bars as possible. 

 **Note:**  The boy can buy the ice cream bars in any order.

Return  *the  **maximum**  number of ice cream bars the boy can buy with* `coins` *coins.* 

You must solve the problem by counting sort.

 

 **Example 1:** 

```
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

```

 **Example 2:** 

```
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.

```

 **Example 3:** 

```
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

```

 

 **Constraints:** 

- costs.length == n
- 1 <= n <= 105
- 1 <= costs[i] <= 105
- 1 <= coins <= 108

## Solution

**Language:** Python  
**Runtime:** 36 ms (beats 93.29%)  
**Memory:** 30.9 MB (beats 86.35%)  
**Submitted:** 2026-10-26T16:30:26.138Z  

```py
class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for cost in costs:
            count[cost] += 1
        bought = 0
        for price in range(1, max_cost + 1):
            if count[price] == 0:
                continue
            can_buy = min(count[price], coins // price)
            bought += can_buy
            coins -= can_buy * price
            if coins < price:
                break
        return bought
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/)