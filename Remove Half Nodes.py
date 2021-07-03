# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        if not A:
            return
        
        if (not A.left and A.right) or (not A.right and A.left):

                
            return self.solve(self.delNode(A))
        
        A.left = self.solve(A.left)
        A.right = self.solve(A.right)
        
        return A
        
    def delNode(self, A):
        #for sure the deleted node will have a single child
        if A.left and not A.right:
            return A.left
        else:
            return A.right
