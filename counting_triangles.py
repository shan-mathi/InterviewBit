from collections import Counter
INT_MAX = 2147483647
#brute force
def counting_triangles(a):
    a.sort()
    l = len(a)
    count=0
    for i in range(l-2):
        s0 = i+1
        s1 = l-1
        while(s0<s1):
            if a[i]+a[s0]> a[s1]:
                count+= s1 - s0
                s1-=1

            else:
                s0 += 1
    return count


    return count






a = list(map(int,input().split()))
print(counting_triangles(a))








