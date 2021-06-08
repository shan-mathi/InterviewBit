from collections import deque
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        
        stack = deque()
        for i in A:
            if i not in ["+","-","*","/"]:
                stack.append(i)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                sol = str(int(eval(val2 + i + val1)))
                stack.append(sol)
        return stack.pop()
