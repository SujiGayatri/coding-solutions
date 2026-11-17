class Solution:
    def getCarries(self, s1, s2):
        # code here
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        count = 0
        while i >= 0 or j >= 0:
            d1 = int(s1[i]) if i >= 0 else 0
            d2 = int(s2[j]) if j >= 0 else 0
            total = d1 + d2 + carry
            if total >= 10:
                count += 1
                carry = 1
            else:
                carry = 0
            i -= 1
            j -= 1
        return count