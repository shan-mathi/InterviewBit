class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        n=A
        dp=[0] * (n + 1)
        dp[0],dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[i-j]*dp[j-1]
        return dp[n]
