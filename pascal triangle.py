class Solution:
    def generate(self, A: int) -> List[List[int]]:
        l=[]
        for i in range(A):
            l.append([1 if j==0 or j==i else l[i-1][j]+l[i-1][j-1] for j in range(i+1)])
        return l
