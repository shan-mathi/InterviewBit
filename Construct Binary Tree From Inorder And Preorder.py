# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, pre_o, in_o):

        if not in_o:
            return None
        
        for i in pre_o:
            if i in in_o:
                v = i
                pre_o.remove(i)
                break
        
        root  = TreeNode(v)
        id = in_o.index(v)
        root.left = self.buildTree(pre_o, in_o[:id])
        root.right = self.buildTree(pre_o, in_o[id+1:])
        return root
        
        
        
        
        
        
	        
	    
