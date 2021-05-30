

#brute force
def all_thrice_excpet_one(A):
    ans=0

    for i in reversed(range(32)):
        count=0
        for j in range(len(A)):
            if A[j]&(1<<i):
                count+=1
        if count%3!=0:
            ans += 1<<i
    return ans






    #id = f.values().index(1)
    #return f.keys()[id]







A = list(map(int,input().split()))
print(all_thrice_excpet_one(A))








