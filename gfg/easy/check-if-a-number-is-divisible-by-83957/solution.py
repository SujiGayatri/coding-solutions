class Solution:
    def isDivBy8(self, s):
        # code here
        num = 0
        for ch in s:
            num = (num * 10 + int(ch)) % 8
        return num == 0