class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        ans = 0
        for i in range(24):
            count = 0
            for num in candidates:
                if num & (1 << i):
                    count += 1
            ans = max(ans, count)
        return ans