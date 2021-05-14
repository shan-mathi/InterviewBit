import math
import string
def lex_rank(A):
    """
    approach: interesting
    
    :param A: a word
    :return: the rank of the word when arranged lexically
    """

    p = 0
    alp = [i for i in A]

    alp.sort()
    print(alp)
    ans = 0
    l = len(A)
    while p < l:
        search = A[p]
        p += 1
        i = alp.index(search)
        alp.remove(search)
        if i!=0:

            ans+= i*math.factorial(l-p)
        
    return ans+1


print(lex_rank('DTNGJPURFHYEW'))






















