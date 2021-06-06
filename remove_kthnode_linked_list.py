# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        
        itr = A
        len=0
        while itr:
            len+=1
            itr = itr.next
        
        if B>=len:
            return A.next
        
        itr=A
        count=0
        while itr:
            count+=1
            if count == len - B:
                itr.next = itr.next.next
                return A
            itr = itr.next
            
