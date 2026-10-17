class Solution:
    def countPairs(self, arr):
        # code here
        freq = {}
        count = 0
        for num in arr:
            if num in freq:
                count += freq[num]
            freq[num] = freq.get(num, 0) + 1
        return count