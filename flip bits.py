class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        #naive approach
        #-1 2 9 -2 4 5 -10 11
        #  l           r
        #1 0 0 1 1 0 0 0 
        #1 1 1 0 0 1 1 1

        #edge case = 0  (done)
        # edge case = 10101010


        if A.count('1')==len(A):
            return []
        

        left,right = -1,-1
        count, max_count = 0,0
        reset = True
        currleft = 0

        for i in range(len(A)):
            if A[i]=='0':
                if reset:
                    currleft = i
                    reset = False
                count+=1
            
            else:
                if count>max_count:
                    max_count = count
                    left = currleft+1
                    right = i
                
                if count>0:
                    count-=1
                else:
                    count=0
                    reset = True

        if count>max_count:
            max_count = count
            left = currleft+1
            right = i+1

        return [left,right]
        

            


                
        

