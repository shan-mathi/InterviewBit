# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    lenn=float('inf')
    def minDepth(self, A, l=1):
        if not A:
            return 0
        
        if not A.left and not A.right:
            self.lenn = min(self.lenn,l)
        
        self.minDepth(A.left, l+1)
        self.minDepth(A.right, l+1)
        
        return self.lenn
        
        
