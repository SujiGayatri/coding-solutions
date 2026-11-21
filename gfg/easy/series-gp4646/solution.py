class Solution:
	def nthTerm(self, a, r, n):
		# code here
		MOD = 1000000007
        return (a * pow(r, n - 1, MOD)) % MOD