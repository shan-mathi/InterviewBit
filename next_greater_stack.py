import collections
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        stack = collections.deque()
        ans = collections.deque()
    
        l = len(A) - 1
        while l >= 0:
            if stack and A[l] < stack[-1]:
                ans.appendleft(stack[-1])
    
            elif stack and A[l] >= stack[-1]:
                while stack and stack[-1] <= A[l]:
                    stack.pop()
                if stack:
                    ans.appendleft(stack[-1])
                else:
                    ans.appendleft(-1)
    
            elif len(stack) == 0:
                ans.appendleft(-1)
            stack.append(A[l])
            l -= 1
        return ans
            
                
            
