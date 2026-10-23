class Solution:

    def maxHeight(self, n: int) -> int:
        """code here"""
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            required = mid * (mid + 1) // 2
            if required <= n:
                left = mid + 1
            else:
                right = mid - 1
        return right