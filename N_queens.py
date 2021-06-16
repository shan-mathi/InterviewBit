def N_queens(n):
    ans=[]

    def back_track(col_array=[]):
        if len(col_array) == n:   #GOAL    ===> if our column length reaches n
            ans.append(col_array[:])
            return

        for i in range(n):       #CHOICES ===> here the choice are all the column values
            col_array.append(i)
            if isValid(col_array):    #CONSTRAINTS ====> sub function; ensure that no thing is right below, and nothing is diagonally opposite
                back_track(col_array)

            col_array.pop()

    def isValid(col_array):
        row_index = len(col_array)-1
        for i in range(row_index):
            dif = abs(col_array[i] - col_array[row_index])
            if dif==0 or dif== row_index - i:
                return False
        return True

    back_track()
    return ans

if __name__ == "__main__":
    n = int(input())
    main=[]
    queens = N_queens(n)
    for i in queens:
        sub=[]
        for j in i:
            sub.append("."*j+ 'Q'+"."*(n-1-j))
        main.append(sub)
    print(main)
