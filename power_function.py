def pow(x, n, d):
    if n==0 and x!=0:
        return 1%d
    elif n==0 and x==0:
        return 0
    ans = power(x, n)
    return ans % d

#main power function
def power(x, n):
    if n==1:
        return x
    elif n%2==0:
        return power(x, n // 2) ** 2
    elif n%2==1:
        return power(x,(n+1)//2)*power(x,(n-1)//2)




x,n,d = map(long,input().split())

print(pow(x,n,d))
