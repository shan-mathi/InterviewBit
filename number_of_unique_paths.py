import math
import string
def number_of_unique_paths(A,B):
    """

    :param A: grid length
    :param B: grid breadth
    :return: number of unique ways to reach final destination
    """
    a= A-1
    b=B-1
    ans = math.factorial(a+b)/(math.factorial(b)*math.factorial(a))
    return ans
print(number_of_unique_paths(3,3))















print(excel_colimn_base(468096))






