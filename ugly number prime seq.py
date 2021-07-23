    def solve(self, A, B, C, D):
        i_A, i_B, i_C = 0, 0, 0
        n_A, n_B, n_C = A, B, C
        arr = [0]*D
        for i in range(D):
            temp = min(n_A, n_B, n_C)
            arr[i] = temp
            if(arr[i] == n_A):
                n_A = A*arr[i_A]
                i_A += 1
            
            if(arr[i] == n_B):
                n_B = B*arr[i_B]
                i_B += 1
            
            if (arr[i] == n_C):
                n_C = C*arr[i_C]
                i_C+=1
            
        return arr
