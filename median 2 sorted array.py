class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2, nums1
            
        
        x = len(nums1)
        y = len(nums2)
        
        flag = (x+y)%2==0
        
        high = x
        low=0
        while low<=high:
            xPartition = (low+high)//2
            yPartition = (x+y+1)//2 - xPartition
            
            maxLeftX = float('-inf') if xPartition==0 else nums1[xPartition-1]
            minRightX = float('inf') if xPartition==x else nums1[xPartition]
            
            maxLeftY = float('-inf') if yPartition==0 else nums2[yPartition-1]
            minRightY = float('inf') if yPartition==y else nums2[yPartition]
            
            if maxLeftX<=minRightY and maxLeftY<=minRightX:
                if not flag:
                    return max(maxLeftX,maxLeftY )
                else:
                    return (max(maxLeftX,maxLeftY) + min(minRightX,minRightY))/2
                
            elif maxLeftX>minRightY:
                high = xPartition-1
            else:
                low = xPartition+1
            
            
            
            
        
