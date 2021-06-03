INT_MAX = 2147483647
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A,B,C):
        i,j,k=0,0,0
        #a,b,c=0,0,0
        res= INT_MAX
        while( i<len(A) and j<len(B) and k<len(C)):
            if min(A[i],B[j],C[k]) == A[i]:
                a=1
                b=0
                c=0
            elif min(A[i],B[j],C[k]) == B[j]:
                b=1
                a=0
                c=0
            else:
                c=1
                a=0
                b=0
    
            if max(A[i],B[j],C[k]) - min(A[i],B[j],C[k]) <= res:
                res = max(A[i],B[j],C[k]) - min(A[i],B[j],C[k])
    
            if a:
                i+=1
            elif b:
                j+=1
            elif c:
                k+=1
    
    
    
    
        return res
