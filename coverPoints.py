def coverPoints(A, B):
    """
    my approach. since it can go diagonal, we can shift the point
    in such a way it needs to travel only the longest side of the 
    rectange. hence we keep adding the longest side values.
    
    :param A:  x coordinates of all the points
    :param B:  y coordinates of all the y points
    :return:  minimum distance to reach to all the diestination points
    """
    l = len(A)
    dist = []
    for i in range(1, l):
        x_dis = abs(A[i] - A[i - 1])
        y_dis = abs(B[i] - B[i - 1])
        dist.append(max(x_dis, y_dis))
    return sum(dist)


A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(coverPoints(A,B))
