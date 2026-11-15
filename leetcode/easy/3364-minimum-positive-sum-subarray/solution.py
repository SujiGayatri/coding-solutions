class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        for i in range(len(nums)):
            total = 0
            for j in range(i, min(i + r, len(nums))):
                total += nums[j]
                length = j - i + 1
                if l <= length <= r and total > 0:
                    min_sum = min(min_sum, total)
        return min_sum if min_sum != float('inf') else -1