class Solution:
    def compareFrac(self, s: str) -> str:
        # code here
        f1, f2 = s.split(", ")

        a, b = map(int, f1.split("/"))
        c, d = map(int, f2.split("/"))

        left = a * d
        right = c * b

        if left > right:
            return f1
        elif right > left:
            return f2
        else:
            return "equal"