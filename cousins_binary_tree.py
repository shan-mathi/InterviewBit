# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        """
        logic: im setting a queue that contains all the nodes of the same level
        i.e both siblings + cousins
        so im colecting all the parents of siblings and cousins
        if a particular parent's child is B then the brothers kids will be the cousins
        
        """
        if not A:
            return []
        
        queue=[A]
        #level = [] #will store values in the same level #2d array, siblings will also be grouped togther
        next_queue=[]
        #result=[]
        #l=0
        parent_node = []
        ans=[]
        
        while queue:   #atleast one node (or one child)
            for node in queue:
                #level.append(node)
                
                if node.left:
                    if node.left.val==B:
                        parent_node = queue
                        parent_node.remove(node)
                        next_queue=[]
                        break
                    next_queue.append(node.left)
                if node.right:
                    if node.right.val==B:
                        parent_node = queue
                        parent_node.remove(node)
                        next_queue=[]
                        break
                    next_queue.append(node.right)
            #print(next_queue)
                
            queue = next_queue
            next_queue=[]
            #result.append(level)
            #level=[]
        #print(parent_node)
        
        for i in parent_node:
            if i.left:
                ans.append(i.left.val)
            if i.right:
                ans.append(i.right.val)
        #print(ans)
        
        return ans
            
                
            
        
