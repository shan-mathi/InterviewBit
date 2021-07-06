class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        line = dict(zip(A,B))
        correct_order= ['x']*len(A)
        index = list(range(len(A)))
        while correct_order.count('x')>0:
            for i in sorted(line):
                count = line[i]
                id = index[count]
                index.pop(count)
                correct_order[id] = i
        return correct_order
