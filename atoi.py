class Solution:
    # @param A : string
    # @return ascii to integer
    def atoi(self, a):
        """
        with overflow conditons,
        
    
        :param S: a string numerical
        :return: converted integer
        """
        pos=True
        if a[0]=='+':
            pos=True
            a=a[1:]
        elif a[0]=='-':
            pos = False
            a=a[1:]
    
    
        ref = '0123456789'
        l = 0
        ans=0
        c=0
        while(l<len(a)):
            if a[l] in ref:
                c+=1
                l += 1
            elif a[l] not in ref:
                break
        for i in range(c):
            ans+= ref.index(a[i])*(10**(c-i-1))
    
    
    
    
        if not pos:
            ans*=-1
            if (abs(ans) > ((1 << 31) - 1)):
                return -1*2147483648
            return ans
        if (abs(ans) > ((1 << 31) - 1)):
            return 2147483647
    
        return ans
