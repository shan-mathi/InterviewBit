class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        #Maximum Absolute Difference
        """
        trick open the absolute and try to see how to optimise keeping the compleity low.
        f(i,j) = | A[i] - A[j] | + | i - j |
        :param A: a list og numbers both pos and negative
        :return: using the above function generate the max value
        """
        l1 =[]
        l2 = []
        for i,v in enumerate(A):
            l1.append(v+i)
            l2.append(v-i)
        m1 = max(l1) - min(l1)
        m2 = max(l2)- min(l2)
        return (max(m1,m2))
