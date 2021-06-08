from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        a = A.split('/')
    
        stack = deque()
        for i in a:
            if i in [""," ","."]:
                continue
            elif i=="..":
                if len(stack)>0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
    
    
        final = "/" + '/'.join(stack)
    
    
    
        return final

    
