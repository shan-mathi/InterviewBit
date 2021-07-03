# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    ans=[]
    def sumNumbers(self, A):
        
        def summer(A,s=''):
            if not A:
                return
            
            s += str(A.val)
            
            if not A.right and not A.left:
                print(s)
                self.ans.append(s)
                #return
                
            if A.left:
                summer(A.left,s)
            if A.right:
                summer(A.right,s)
            
            s = s[:-1]
            
            #return
        summer(A)
        return (sum(map(int,self.ans)))%1003
            
            
