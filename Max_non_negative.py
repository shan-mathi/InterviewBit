def Max_non_negative(A):
    """
    aim is to travesre the list and flag the points that are negative, ans clculate the sum
    that exceeds the previous sum and change the indices accordingly
    to print the reqd. sunset.

    :param A:
    :return: returns a continous list of maximum non negative number
    """
    
    """
    Example Input
Input 1:

 A = [1, 2, 5, -7, 2, 3]
Input 2:

 A = [10, -1, 2, 3, -4, 100]


Example Output
Output 1:

 [1, 2, 5]
Output 2:

 [100]
    """


    set=[]
    summ=[]
    all_set=[]
    for j in A:
        if j<0:

            summ.append(sum(set))
            all_set.append(set)
            set=[]
        else:
            set.append(j)
    summ.append(sum(set))
    all_set.append(set)

    i = summ.index(max(summ))
    return all_set[i]



    return ans

A = list(map(int,input().split()))
print(Max_non_negative(A))





