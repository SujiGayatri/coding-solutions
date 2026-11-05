class Solution:
    def leastAvg(self, arr, k):
        # code here
        n = len(arr)
        window_sum = sum(arr[:k])
        min_sum = window_sum
        ans = 0
        for i in range(k, n):
            window_sum += arr[i] - arr[i-k]
            if window_sum < min_sum:
                min_sum = window_sum
                ans = i - k + 1
        return ans + 1