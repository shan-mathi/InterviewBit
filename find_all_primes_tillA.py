# seive of Eratosthenes--- more optimised O(sqrt(n)*logn)
def seive(A):

    sei = [True]*(A+1)
    for i in range(2,int(A**0.5)+1):


        for j in range(i**2,A+1,i):
            sei[j]=False
    ans=[]


    for i,v in enumerate(sei[2:]):
        if v:
            ans.append(i+2)
    return ans


print(seive(25))
