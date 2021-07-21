class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        n = len(A)

        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = A[0]
        suffix[-1]=A[-1]

        for i in range(1,n):
            prefix[i] = max(prefix[i-1], A[i])
        #print(prefix)
        
        for i in reversed(range(n-1)):
            suffix[i] = min(suffix[i+1], A[i])
        #print(suffix)
        for i in range(1,n-1):
            if prefix[i]==A[i] and prefix[i-1]!=prefix[i]:
                if A[i]==suffix[i] and suffix[i+1]!=suffix[i]:
                    return 1
        return 0

        
