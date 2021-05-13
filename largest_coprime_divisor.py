import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        #largets factor of A is A, if A is divisdible by A then remove the common factor
        while(math.gcd(A,B)!=1):
            A= A//math.gcd(A,B)

        return A
