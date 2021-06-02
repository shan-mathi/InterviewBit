class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, a):

        q=0
        t=1
        for i in range(1,len(a)):
            if a[i]!=a[q]:
                q=t
                a[i],a[t]=a[t],a[i]
                t+=1
        return t
