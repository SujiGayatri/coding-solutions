class Solution:
    def shortestDistance(self, s: list[str], word1: str, word2: str) -> int:
        # code here
        i1 = -1
        i2 = -1
        ans = float('inf')

        for i in range(len(s)):
            if s[i] == word1:
                i1 = i

            if s[i] == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1 - i2))

        if ans == float('inf'):
            return -1

        return ans