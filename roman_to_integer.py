import math

#brute force
def roman_to_integer(n):

    ans=0

    hash = {'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1}
    i=0
    while( i< len(n)):
        if i+1<len(n) and hash[n[i+1]]> hash[n[i]]:
            ans+= hash[n[i+1]] - hash[n[i]]
            i+=2
        else:
            ans+= hash[n[i]]
            i+=1
    return ans



n = str(input())
print(roman_to_integer(n))









