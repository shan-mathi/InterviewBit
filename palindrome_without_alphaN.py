import string
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, s):
        s = s.lower()
        l = len(s)
        low=0
        high = l-1
        ref="abcdefghijklmnopqrstuvwxyz0123456789"
        while(low<=high):
            if s[low] in ref and s[high] in ref:
                if s[low]==s[high]:
                    low+=1
                    high-=1
                else:
                    return 0
            elif s[low] not in ref and s[high] not in ref:
                low+=1
                high-=1
            elif s[low] not in ref:
                low+=1
            elif s[high] not in ref:
                high-=1
        return 1

