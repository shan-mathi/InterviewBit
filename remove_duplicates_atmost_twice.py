class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i=1
        t=0
        f=1
    
        while i<len(A):
            if A[i]==A[t] and f<2:
                t+=1
                A[t]=A[i]
                f+=1
                i+=1
            elif A[i]==A[t]:
                i+=1
                f+=1
            elif A[i]!=A[t]:
                t+=1
                A[t]=A[i]
                i+=1
                f=1
        return t+1
