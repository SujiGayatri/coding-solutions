class Solution:
    def canReach(self, a, b, x):
        # code here
        min_moves = abs(a) + abs(b)
        return x >= min_moves and (x - min_moves) % 2 == 0