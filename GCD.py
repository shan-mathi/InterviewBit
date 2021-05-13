
def gcd(A,B):
    A,B = max(A,B), min(A,B)
    if B==0:
        return 1

    while(A%B!=0):
        temp=B

        B= A%B
        A=temp



    return B
print(gcd(56,120))















print(excel_colimn_base(468096))






