class Solution:
    def constructArr(self, arr):
        # code here
        m = len(arr)
        if m == 1:
            return [1, arr[0] - 1]
        n = int((1 + (1 + 8 * m) ** 0.5) / 2)
        res = [0] * n
        res[0] = (arr[0] + arr[1] - arr[n - 1]) // 2
        res[1] = arr[0] - res[0]
        for i in range(2, n):
            res[i] = arr[i - 1] - res[0]
        return res