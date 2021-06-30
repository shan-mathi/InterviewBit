# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        
        def sub_validate(A, upper=float('-inf'), lower=float('inf')):
            if not A:
                return True
            
            if A.val>=upper or A.val<=lower:
                return False
                
            return sub_validate(A.left, A.val, lower) and sub_validate(A.right, upper, a.val)
        
        
        if sub_validate(A):
            return 1
        
        else:
            return 0
               
               
        

        
        
            
            
        
        
        
        

        

           
