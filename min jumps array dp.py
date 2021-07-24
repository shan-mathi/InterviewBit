import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        if A==[]:
            return -1

        if A[0]>len(A):
            return 1+self.jump(A[1:])
        else:
            return 1 + min(self.jump(A[1:]),
                            self.jump(A[A[0]:]))

