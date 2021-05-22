#trick is to use split function

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a = A.split('.')
        b = B.split('.')
        if len(a)>len(b):
            b+=['0']*(len(a)-len(b))
        else:
            a+=['0']*(len(b)-len(a))
        for i,j in zip(a,b):
            if int(i)==int(j):
                continue
            elif int(i)>int(j):
                return 1
            elif int(i)<int(j):
                return -1
        return 0
