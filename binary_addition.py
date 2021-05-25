class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        cy=0
        ans=''
        if len(B)>len(A):
            A,B = B,A
    
        B = '0'*(len(A)-len(B)) + B
    
        A = A[::-1]
        B= B[::-1]
        for a,b in zip(A,B):
            if int(a) + int(b) +cy >2:
                ans+= '1'
                cy=1
            elif int(a) + int(b) +cy ==2:
                ans +='0'
                cy=1
            elif int(a) + int(b) +cy <2:
                ans+= str(int(a) + int(b) +cy )
                cy=0
        if cy:
            ans+='1'
        ans= ans[::-1]
        return int(ans)
