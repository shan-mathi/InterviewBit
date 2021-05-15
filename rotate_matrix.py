class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        l = len(A)
        for i in range(l//2):
            A[i], A[l-i-1] = A[l-i-1], A[i]
        ans = [[A[j][i] for j in range(l)] for i in range(len(A[0]))]
        return ans
