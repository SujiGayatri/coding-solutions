class Solution:
    def uneatenLeaves(self, arr: list[int], m: int) -> int:
        # code here
        eaten = [False] * (m + 1)
        for k in set(arr):
            for leaf in range(1, m + 1, k):
                eaten[leaf] = True
        return eaten[1:].count(False)