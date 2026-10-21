class Solution:
    def totalJumps(self, arr, x, y):
        # code here
        jumps = 0
        net = x - y
        for h in arr:
            if h <= x:
                jumps += 1
            else:
                jumps += 1 + (h - x + net - 1) // net
        return jumps