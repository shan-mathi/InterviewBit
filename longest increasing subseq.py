class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
		#dayummm this solution is damn smart!
		#so basically sort the list and find the lcs of this and that

		B = sorted(set(A))
		n = len(A)
		m = len(B)
		dp = [[0 for i in range(n+1)] for j in range(m+1)]

		for j in range(1,m+1):
			for i in range(1,n+1):
				if A[i-1]==B[j-1]:
					dp[j][i] = 1 + dp[j-1][i-1]
				else:
					dp[j][i] = max(dp[j-1][i],dp[j][i-1])
		return dp[m][n]
	
	def solve_method2(self, A):
		
            n = len(A)
            dp = [1]*n
                
            for i in range(1,n):
                for j in range(0,i):
                    if A[j] < A[i]:
                        dp[i] = max(dp[i] , dp[j] + 1)
                
            return dp
        
