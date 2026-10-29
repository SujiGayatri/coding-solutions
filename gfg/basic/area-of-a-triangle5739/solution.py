class Solution:
    def findArea(self, a, b, c):
        # code here
        if a + b <= c or a + c <= b or b + c <= a:
            return 0.000
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        area = int(area * 1000) / 1000
        return area