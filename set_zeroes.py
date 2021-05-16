
def set_zeros(A):
    R = len(A)
    C = len(A[0])
    r = []
    c = [1]*C
    for i in range(R):
        if 0 in A[i]:

            for j in range(C):
                if A[i][j]==0:
                    c[j]=0
            A[i]=[0]*C
        else:
            r.append(i)

    for i in r:
        for j in range(C):
                if not c[j]:
                    A[i][j]=0
    return A






A=    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]


print(set_zeros(A))
