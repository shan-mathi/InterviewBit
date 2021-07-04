# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    
    def verticalOrderTraversal(self, A):
        vr={}
        def vertical(A,c=0):
            if not A:
                return
            if c in vr:
                
                vr[c].append(A.val)
                #print(self.vr)
            else:
                vr[c]=[A.val]
                #print(self.vr)
            
            vertical(A.left, c+1)
            vertical(A.right, c-1)
        
        vertical(A)
        c = list(vr.keys())
        ans=[]
        c.sort()
        for i in reversed(c):
            
            ans.append(vr[i])
        #print(ans)
        
        return ans
    
        
        
        
