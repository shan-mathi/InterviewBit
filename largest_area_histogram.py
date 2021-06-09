from collections import deque
class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        area=0
        stack = deque()
        
        for i, h in enumerate(A):
            start = i
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                area = max(area, height*(i-index))
                start = index
            stack.append((start,h))
        
        for i, h in stack:
            area = max(area, h*(len(A)-i))
        
        return area
            
        
                
            
