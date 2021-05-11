def primesum(A):
    """
    every even number can be represented by sum of 2 prime numbers.
    here we create a list of all primes less than A. and check if i and A-i are in the list.
    :param A: even postive number
    :return: a pair of prime numbers
    """
    if A == 4:
        return [2, 2]

    sei = [False]*2+ [True]*(A-1)
    for i in range(2,int(A**0.5)+1):


        for j in range(i**2,A+1,i):
            sei[j]=False


    for i in range(len(ans)):
        if ans[A-i] and ans[i]:
            return [i,A-i]









A = int(input())
print(primesum(A))






