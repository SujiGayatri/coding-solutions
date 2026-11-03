class Solution:
    def maxDiamonds(self, arr, k):
        #code here 
        arr = [-x for x in arr]
        heapq.heapify(arr)
        total = 0
        for _ in range(k):
            max_diamond = -heapq.heappop(arr)
            total += max_diamond
            remaining = max_diamond // 2
            heapq.heappush(arr, -remaining)
        return total