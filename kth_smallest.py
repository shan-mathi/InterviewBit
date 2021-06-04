from collections import Counter
INT_MAX = 2147483647
#brute force
def kth_smallest(a,k):
    l = len(a)
    low =min(a)
    high = max(a)

    while(low<=high):
        mid = low + (high - low)//2
        count_less, count_equal =0,0

        for i in range(l):
            if a[i]< mid:
                count_less+=1
            elif a[i]==mid:
                count_equal+=1

        if count_less<k and (count_less + count_equal) >=k:
            return mid

        elif count_less>= k:
            high = mid-1

        elif (count_less < k and count_less + count_equal < k):
            low = mid+1





a = list(map(int,input().split(', ')))
k = int(input())

print(kth_smallest(a, k))








