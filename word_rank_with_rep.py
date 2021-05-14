import math
class Solution:
    # @param A : string
    # @return an integer
    
    def fac(self,li):
        p=1
        for i in li:
            if i>1:
                p*= math.factorial(i)
        return p

    def duplicate(self,i,alp):
    
        d=alp.copy()
        s = list(alp.keys())[i]
        if d[s]>1:
            d[s]-=1
        else:
            d.pop(s)
        v = list(d.values())
        ans = math.factorial(sum(v)) / self.fac(v)
    
        return ans
        
    def findRank(self, A):
        """
        approach: interesting
    
        :param A: a word
        :return: the rank of the word when arranged lexically
        """
    
        p = 0
        alpha = [i for i in A]
        alpha.sort()
        keys=list(set(alpha))
        keys.sort()
        v= [alpha.count(i) for i in keys]
        alp = dict(zip(keys,v))
    

    
        ans = 0
        l = len(A)
        while p < l:
            search = A[p]
            p += 1
            i = list(alp.keys()).index(search)
    
    
            if i!=0:
                v= list(alp.values())
                #ans+= i* math.factorial(sum(v))/fac(v)
                for j in range(i):
                    ans+= self.duplicate(j,alp)
    
            if alp[search]>1:
                alp[search]-=1
            else:
                alp.pop(search)
    
    
        return ans+1
