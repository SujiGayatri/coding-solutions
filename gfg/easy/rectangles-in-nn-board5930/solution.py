class Solution:
    def rectanglesInChessBoard(self, N):
        # code here
        total_rectangles = (N * N * (N + 1) * (N + 1)) // 4
        total_squares = (N * (N + 1) * (2 * N + 1)) // 6
        return total_rectangles - total_squares