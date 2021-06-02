class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i=0
        j=0
        ans=[]
        while( i<len(A) and j<len(B)):
            if B[j]<A[i]:
                 j+=1
            elif B[j]>A[i]:
                i+=1
            elif B[j]==A[i]:
                ans.append(B[j])
                j+=1
                i+=1
        return ans
