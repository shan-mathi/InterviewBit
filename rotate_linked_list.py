# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        itr = A
        len = 0
        while itr:
            len += 1
            itr = itr.next
        n = B%len
        if n==0:
            return A
        n = len - n


        
        count =0
        itr = A
        while itr:
            count+=1
            if count ==n:
                var = itr.next
                itr.next = None
                itr = var
                continue
            elif itr.next==None:
                itr.next = A
                return var
            
            itr = itr.next

       
            
               
       
       
            
