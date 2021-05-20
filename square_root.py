# this is using the famous babylon method to find the square root
""" 
Make an initial guess. Guess any positive number x0.
Improve the guess. Apply the formula x1 = (x0 + S / x0) / 2. The number x1 is a better approximation to sqrt(S).
Iterate until convergence. Apply the formula xn+1 = (xn + S / xn) / 2 until the process converges. Convergence is achieved when the digits of xn+1 and xn agree to as many decimal places as you desire.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==0:
            return 0
        elif A in range(1,4):
            return 1
        else:
            x = A//2
            x1 = (x + A/x)/2
            while(int(x)>int(x1)):
                x = x1
                x1 = (x1 + A/x1)/2
            if int(x)==int(x1):
                return int(x)


