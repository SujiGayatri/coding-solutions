class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort(reverse=True)
        total = 0
        n = len(piles)
        for i in range(1, 2 * n // 3, 2):
            total += piles[i]
        return total