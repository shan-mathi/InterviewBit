def spiral(A):
    """
    there will be 4 pointers called top,bottom,left, right
    keeping one fixed the others will travers all following a single while loop
    doing the same way as following a aprial staircase
    ther will also be 4 directoion
    0: l to r
    1: u to d
    2: r to l
    3: d to u

    :param A: a square matrix
    :return: a linear array with the spiral elements
    """
    l=len(A)
    top,left=0,0
    right = len(A[0])-1
    bottom = l-1
    dir=0
    ans=[]

    while(top<=bottom and left<=right):

        if dir==0:
            for i in range(left,right+1):
                ans.append(A[top][i])
            top+=1
            dir+=1
        elif dir==1:
            for i in range(top,bottom+1):
                ans.append(A[i][right])
            right-=1
            dir+=1
        elif dir==2:
            #r to l
            for i in range(right,left-1,-1):
                ans.append(A[bottom][i])
            bottom-=1
            dir+=1
        elif dir==3:
            #d to u
            for i in range(bottom,top-1,-1):
                ans.append(A[i][left])
            left+=1
            dir=0
    return ans
