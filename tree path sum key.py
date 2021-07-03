# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    ans=0
    
    def hasPathSum(self, A, B):
        if not A:
            return 0
        
        if not A.left and not A.right:
            return 1 if A.val==B else 0
        
        return self.hasPathSum(A.left, B-A.val) or self.hasPathSum(A.right, B-A.val )

                
                
                    
        
