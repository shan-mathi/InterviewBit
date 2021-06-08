# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        count =0
        mid = A
        itr = A
        while itr:
            if count%2==1:
                mid = mid.next
            itr = itr.next
            count+=1
        
        prev = None
        itr = mid
        while itr:
            temp = itr.next
            itr.next = prev
            prev = itr
            itr = temp
        rev = prev
        ib = rev
        ia = A
        while ib:
            tempa = ia.next
            if tempa == None:
                ia = ib
                return A
            if tempa ==ib:
                return A
            ia.next = ib
            tempb = ib.next
            ib.next = tempa
            ia = tempa
            ib = tempb
        return A
        
        
        
        
        
        
