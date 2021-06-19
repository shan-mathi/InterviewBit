from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        a = list(A)
        a.sort()
        ans={}
        for i in a:
            if i in ans:
                return 1
            else:
                ans[B+i]=1
        return 0
            

        
