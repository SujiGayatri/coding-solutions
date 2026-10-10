import math
class Solution:
    def maxVolume(self, p: int, a: int) -> float:
        # code here
        s = p / 4
        q = a / 2
        d = math.sqrt(s * s - 3 * q)
        t1 = (s + d) / 3
        t2 = (s - d) / 3
        volumes = []
        for t in (t1, t2):
            z = s - 2 * t
            if t > 0 and z > 0:
                volumes.append(t * t * z)
        return round(max(volumes), 2)