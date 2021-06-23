class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        xor =0
        freq = {}
        """
        a = [4,2,2,6,4] k =6
        b = [    ]        b is overall xor value a is the prefix xor value..... 
        k will be the sufix xor value a = b^k we have calculated the freq of all
        prefix values.. k is the sufix value.
        freq = {(xor val): freq}
        """
        
        for i in A:
            xor = xor^i
            
            if xor == B:
                count+=1
            
            if xor^B in freq:
                count+=freq[xor^B]
            
            if xor in freq:
                freq[xor]+=1
            else:
                freq[xor]=1
            
        return count
            
            
            
            
            
            

