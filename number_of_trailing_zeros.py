import math
import string
def number_of_trailing_zeros(A):
    """
    
    :param A: integer A>0
    :return: number of trailing zeros in A!
    """
    
    pow = int(math.log(A,5))
    ans=0
    while(pow):
        ans+= A//(5**pow)
        pow-=1

    return ans

print(number_of_trailing_zeros(9247))
