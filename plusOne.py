class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        """
    
        :param A: an array that represntes a number
        :return: a list
        """
        l = len(A)
        n_str=''
        for i in A:
            n_str+=str(i)
        n_incr = str(int(n_str)+1)
        ans=[]
        for i in n_incr:
            ans.append(int(i))
        return ans
