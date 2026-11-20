class Solution:
    def getSum(self, l: list[int], r: list[int]) -> list[int]:
        # code here
        n = max(r)
        arr = [0] * (n + 1)
        for p in range(2, n + 1):
            if arr[p] == 0:
                for j in range(p, n + 1, p):
                    arr[j] += p
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + arr[i]
        ans = []
        for i in range(len(l)):
            ans.append(prefix[r[i]] - prefix[l[i] - 1])
        return ans