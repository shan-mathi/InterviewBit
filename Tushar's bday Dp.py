class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, A, B, C):
        cap= max(A)
        n = len(B)
        dp = [[0 for i in range(cap+1)] for j in range(n+1)]
        
        for i in range(cap+1):
            dp[0][i] = float('inf')
            #dp[1][i] = i
        
        for i in range(1, n+1):
            for j in range(1,cap+1):
                if j>=B[i-1]:
                    dp[i][j]= min(dp[i-1][j], C[i-1]+dp[i][j-B[i-1]])
                else:
                    dp[i][j]= dp[i-1][j]
        summ=0
        for c in A:
            summ+=dp[n][c]
        return summ
