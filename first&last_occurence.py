class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        ans = []
    
        low = 0
        high = len(A) - 1
        res =-1
        # first occurence
        while (low <= high):
            mid = (low + high) // 2
            if A[mid] > B:
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
            elif A[mid] == B:
                res = mid
                high = mid - 1
        ans.append(res)
    
        low = 0
        high = len(A) - 1
        res = -1
        # second occurence
        while (low <= high):
            mid = (low + high) // 2
            if A[mid] > B:
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
            elif A[mid] == B:
                res = mid
                low = mid+1
        ans.append(res)
        return ans
