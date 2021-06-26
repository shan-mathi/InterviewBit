class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        ref = {}
        #A = list(A)
        for i in range(len(A)):
            if "".join(sorted(A[i])) in ref:
                ref["".join(sorted(A[i]))].append(i + 1)
            else:
                ref["".join(sorted(A[i]))] = [i + 1]
    
        return list(ref.values())
        
