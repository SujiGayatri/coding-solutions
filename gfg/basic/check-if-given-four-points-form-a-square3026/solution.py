class Solution:
    def isSquare(self, points):    
        #code here
        def dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        distances = []
        for i in range(4):
           for j in range(i + 1, 4):
               distances.append(dist(points[i], points[j]))

        distances.sort()
        return (
               distances[0] > 0 and
               distances[0] == distances[1] == distances[2] == distances[3] and
               distances[4] == distances[5] and
               distances[4] == 2 * distances[0]
           )