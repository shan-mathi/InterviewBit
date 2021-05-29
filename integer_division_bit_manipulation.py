"""
approach is we are trying to represnt the dividend in a binary format. say 36/3 =12
12 is 1100 in binary
so we cal also say that 3*(8 + 4 + 0 + 0) = 36
so we keep removing the biggest power of 2 *b that is less than A.
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        if A==-2147483648 and B==-1:
            return 2147483647

        sign=1
    
        if (A<0)^(B<0):
            sign =-1
        
        a,b = abs(A),abs(B)

    
        res=0
        while( a>=b):
            x=0
            while(a >= b<<1<<x):
                x+=1
            res += 1<<x
            a-= b<<x
        return res*sign
