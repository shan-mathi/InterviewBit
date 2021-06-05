# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        #tryin to over write instead of new memory location
        itr = A
        count=[0,0]
        while itr:
            count[itr.val]+=1
            itr = itr.next
        
        itr = A
        i=0
        while itr:
            if count[i]==0:
                i+=1
            else:
                itr.val = i
                count[i]-=1
                itr = itr.next
        return A
        
            

