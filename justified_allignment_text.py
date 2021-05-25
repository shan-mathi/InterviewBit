import math

#brute force
def justified_text_alignment(A,B):
    """

    :param A: a list of words from a senctence
    :param B: L number of characters regquired per line
    :return: n lines that are aligned and justifed equally spaced
    """

    main=[]
    sub=[]
    ans=[]
    for i in A:
        if sub==[]:
            sub.append(i)
            l = len(i)
        elif l+len(i)+1<=B:
            sub.append(i)
            l +=len(i)+1
        elif l+len(i)+1>B:
            main.append(sub)
            sub=[i]
            l=len(i)
    main.append(sub)

    for line in main:
        words = len(line)
        c_count = len("".join(line))
        extras = B - c_count
        if words==1:
            a = line[0] + ' '*(B-len(line[0]))
        else:
            space = extras//(words-1)
            rem = extras%(words-1)
            k=0
            while (rem>0):
                line[k] = line[k]+ ' '
                rem-=1
                k+=1
            a = (" "*space).join(line)


        ans.append(a)




    return ans #cooooooooool


A = ["the", "quick", "brown", "fox", "jumped", "over", "the","lazy","fox"]
B=24
print(justified_text_alignment(A,B))








