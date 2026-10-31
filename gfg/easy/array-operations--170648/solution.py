class Solution:
    def arrayOperations(self, arr: list[int]) -> int:
        # code here 
        if 0 not in arr:
            return -1
        operations = 0
        in_group = False
        for x in arr:
            if x != 0:
                if not in_group:
                    operations += 1
                    in_group = True
            else:
                in_group = False
        return operations