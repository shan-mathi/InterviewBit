# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
	    k=[0]
	    ans=[0]
        def in_order(A):
            elements=[]
    
            #print left of subtree go all the way to leaf node
            if A.left:
                elements += in_order(A.left)
            
            k[0]+=1
            if k[0]==B:
                ans[0]= A.val
                
                
    
            v = A.val
            elements.append(v)
    
            if A.right:
                elements += in_order(A.right)    #we are returning elements so we are basically appeningn the returned value of those sub nodes
    
            return elements
        
        l = in_order(A)
        return ans[0]
