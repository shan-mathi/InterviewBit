def next_largest_number(A):
    """
    
    :param A: a string numner
    
    :return: the smallest next largest number
    """

    if len(A)==1:
        return -1
    l=len(A)-2
    ans=""
    while(l>=0):
        l1 = [int(i) for i in A[l:]]
        if max(l1)==l1[0]:
            l-=1
            continue
        else:
            ctrl = l1[0]
            l1.sort()
            ans+=A[:l]
            for i in l1:
                if i>ctrl:
                    ans+=str(i)
                    l1.remove(i)
                    break
            for j in l1:
                ans+=str(j)
            break
    if l>=0:
        return ans
    else:
        return -1








A = str(input())
print(next_largest_number(A))
