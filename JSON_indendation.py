import math

#brute force
def json_indendation(S):
    """

    :param S: a string
    :return: an indendation answer to prettify the string
    """
    ans= S[0] + '\n\t'
    count=1
    for i in S[1:]:
        if i =='{' or i =='[':

            ans+= '\n'+ '\t'*count + i+ '\n' + '\t'*(count+1)
            count+=1
        elif i==',':
            ans+=',\n' + '\t'*count
        elif i=='}' or i ==']':
            count-=1
            ans+= '\n'+ '\t'*count + i
        else:
            ans+=i
    return ans



S= str(input())

print(json_indendation(S))








