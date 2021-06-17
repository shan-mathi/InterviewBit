class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        ans=[]
        x = 2**A
        for i in range(x):    #divide word into twos...
            j = i//2
            ans.append(i^j)   #gray code will be the XOR of the number with its integer half value
        return ans
        
