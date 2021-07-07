class Solution:
	# @param A : list of strings
	# @return a list of strings
	def prefix(self, Input):
	    """
	    Input: [zebra, dog, duck, dove]
        Output: {z, dog, du, dov}
        where we can see that
        zebra = z
        dog = dog
        duck = du
        dove = dov
	    """
	    ans=[]
	    
	    for word in Input:
            i=0
            while i<len(word):
                prev=i
                for other in Input:
                    if other==word:
                        continue
                    else:
                        if word[:i]==other[:i]:
                            i+=1
                            break
                if i==prev:
                    break
	           
            ans.append(word[:i])
            
        #print(ans)
        return ans
	            
	    
