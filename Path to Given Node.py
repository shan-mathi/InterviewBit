# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def __init__(self):
        self.path = []
    def solve(self, A, B):

        #path.append(A.val)
        def findPath(node, key):
            if not node: #or path[-1]==key:
                return
            
            self.path.append(node.val)
            if node.val != key:
                findPath(node.left,key)
                findPath(node.right, key)
                if self.path[-1]!=key:
                    self.path.pop()
                
            

            return
        
        findPath(A,B)
        return self.path

            
            
            
