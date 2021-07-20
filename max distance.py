class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        """
        suffix array= it collects the maximum elements like a filter dine during zone refining
        and we compare this to our origianl array(A).
        if A[i]<S[j].. then a bigger number is waiting for us in the end. j+=1
        else:
            we crossed a big element therefore i+=1

        also 
        O(N) yay!
        """
        n = len(A)
        S = [0]*len(A)
        S[-1] = A[-1]
        for i in reversed(range(n-1)):
            S[i] = max(S[i+1],A[i])
        
        #S is the suffix array
        i,j=0,0
        ans_max = 0
        while i<n and j<n:
            if A[i]<=S[j]:
                ans_max = max(ans_max, j-i)
                j+=1
            else:
                i+=1
        return ans_max


                

