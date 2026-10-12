# Rectangles in  N*N Board

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Find total number of Rectangles (excluding squares) in a  **N*N**  chessboard.

 **Example 1:** 

```
Input:
N = 1
Output:
0
Explanation:
There is only 1 square on a 1*1 chess
board. There are no Proper Rectangles.
```

 **Example 2:** 

```
Input:
N = 2
Output:
4
Explanation:
There are 4 rectangles in a 2*2 chessboard.
```

 

 **Your Task:** 
You don't need to read input or print anything. Your task is to complete the function  **rectanglesInChessBoard()**  which takes an Integer N as input and returns the number of rectangles in a N*N chess board.

 

 **Expected Time Complexity:**  O(1)
 **Expected Auxiliary Space:**  O(1)

 

 **Constraints:** 
1 <= N <= 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T17:19:31.559Z  

```py
class Solution:
    def rectanglesInChessBoard(self, N):
        # code here
        total_rectangles = (N * N * (N + 1) * (N + 1)) // 4
        total_squares = (N * (N + 1) * (2 * N + 1)) // 6
        return total_rectangles - total_squares
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/rectangles-in-nn-board5930/1)