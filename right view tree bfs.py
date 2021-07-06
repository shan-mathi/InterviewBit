# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        depth={}
        def traversal(A,l=0):
            if not A:
                return
            
            if l not in depth:
                depth[l]= [A.val]
            
            else:
                depth[l].append(A.val)
            
            traversal(A.left,l+1)
            traversal(A.right,l+1)
            
            return
        
        traversal(A)
        ans=[]
        for i in depth:
            ans.append(depth[i][-1])
            
            
            
        return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
