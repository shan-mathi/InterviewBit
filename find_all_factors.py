class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        """
        using the most optimal method i.e O(sqrt(n))
    
        :param A: a number
        :return: list of all its factors
        """
    
        s = int(A**0.5)
        ans=[]

        for i in range(1,s+1):
            if A%i==0:
                ans.append(i)
                if A/i not in ans:
                    ans.append(int(A/i))
        ans.sort()
        return ans
