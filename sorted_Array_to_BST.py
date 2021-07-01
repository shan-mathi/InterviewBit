# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree

    
    def sortedArrayToBST(self, A):
        #2 pointer method
        #         ^    ^
        # [1,2,3,4,5,6,7,8,9]
        if not A:
            return None
        
        A = list(A)
        
        mid = len(A)//2
        root = TreeNode(A[mid])
        root.right = self.sortedArrayToBST(A[mid+1:])
        root.left = self.sortedArrayToBST(A[:mid])
        
        return root
        

            
            
            
