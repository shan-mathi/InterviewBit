class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.maX = float('-inf')
        
    
    def maxPathSum(self, A):
        #using DFS
        #global maX

        

        def dfs(node):
            
            if not node:
                return 0
            
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            cur_val = node.val

            self.maX = max(left_val+cur_val , right_val+cur_val, cur_val,left_val+right_val+cur_val, self.maX)
            return max(left_val, right_val) + cur_val
        
        ans = dfs(A)
        return self.maX
