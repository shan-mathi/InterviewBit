class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if B==0 and A==0:
            return 0
        if B==0:
            return 1
        if B%2==0:
            res = self.Mod(A, B//2, C)
            return (res**2)%C
        else:
            res = self.Mod(A,B-1, C)
            return ((A%C)*res)%C
