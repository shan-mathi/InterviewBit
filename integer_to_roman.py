import math

#brute force
def integer_to_roman(n):

    ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thousands =["","M","MM","MMM"]

    ans = thousands[n//1000] + hundreds[(n%1000)//100] + tens[(n%100)//10] + ones[(n%10)]

    return ans

n = int(input())
print(integer_to_roman(n))









