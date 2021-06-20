class Solution:
    # @param x: list of integers
    # @return a list of integers
    def lszero(self, x):
        
        #
        """
         x = [ 1, 2, -3, 3 ]
        ans = [1,2,-3]
        
        summ = [1, 3, 0, 3]
        summ==0
        if i+1 > start - end:
        start =i
        end -1
        

        
        
        dict = { -1: 0, 1:1,     }
        start, end = 0,0
        
        """
        
        summ=0
        dictt = {}
        start, end = 0,0
        
        for i in range(len(x)):
            summ+=x[i]
            
            if summ==0:
                if i+1 > start - end:
                    start = i
                    end = -1
                continue
            
            
            if summ not in dictt:
                dictt[summ]= i
            
            else:
                if i - dictt[summ] > start - end:
                    start = i
                    end = dictt[summ]
            
        return x[end+1: start+1]
                
                
                    
                

                        
                

                    
