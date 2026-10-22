class Solution:
    def checkDoorStatus(self, n: int) -> list[int]:
       # Code here
        result = []
        for door in range(1, n + 1):
            root = int(door ** 0.5)
            if root * root == door:
                result.append(1)
            else:
                result.append(0)
        return result