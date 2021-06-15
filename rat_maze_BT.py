def isValid(x, y, n, arr):
    if x<n and y<n:
        if arr[x][y]==1:
            return True
        else:
            return False
    else:
        return False

def RatinMaze(x, y, arr, solarr, n):
    #base condition
    if x==n-1 and y==n-1:
        solarr[x][y]='1'
        return True


    if isValid(x, y, n, arr):
        solarr[x][y]='1'
        #checking right path
        if RatinMaze(x, y+1, arr, solarr, n):
            return True
        #checking if down path is valid
        if RatinMaze(x+1, y, arr, solarr, n):
            return True

        #if neither is true then we backtrack and change solarr
        solarr[x][y]='0'
        return False
    return False

if __name__ == "__main__":
    n = int(input("enter the size of maze"))
    print("enter values")
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    solarr=[]
    for i in range(n):
        s = '0'*n
        solarr.append(list(s))
    if RatinMaze(0,0, arr,solarr,n):
        for i in range(n):
            print(" ".join(solarr[i]))
    else:
        print("no solution")

