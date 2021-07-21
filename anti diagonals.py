class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        """
        1 2 3 5
        4 5 6 7
        7 8 9 8
        9 1 2 3
        [[0,0],    sum = 0
        [0,1],[1,0], sum = 1
        [0,2],[1,1],[2,0], sum = 2
        [1,2],[2,1], sum = 3
        [2,2]] sum = 4

        table of size N will have 2n - 1 i.e 0,1,2,...2n-1

               
        """
        ans=[]
        n=len(A)
        for i in range(2*n-1):
            sub=[]
            for j in range(n):
                if j<n and i-j>=0 and i-j<n:
                    sub.append(A[j][i-j])
            ans.append(sub)
        return ans
