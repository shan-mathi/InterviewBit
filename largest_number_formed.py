def arrange(A):
    li = list(map(str,A))
    li.sort()
    l = len(A)
    for i in range(l):
        for j in range(i,l):
            first = li[i]+li[j]
            second = li[j]+li[i]
            if second>first:
                li[j],li[i]= li[i], li[j]
    ans = "".join(li)
    return int(ans)


print(arrange([0,0,0,0,0]))
