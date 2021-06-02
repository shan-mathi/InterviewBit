class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, k):
        start,good,bad,res = 0,0,0,0
    
        for i in A:
            if i==1:
                good+=1
            else:
                bad+=1
            while(bad>k):
                if A[start]==1:
                    good-=1
                else:
                    bad-=1
                start+=1
            res = max(res, good+bad)
        return res
