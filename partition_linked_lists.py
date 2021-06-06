# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def partition(self, A, B):

	    
	    if A.val>= B:
	        prev = ListNode(None)
	        prev.next = A

        else:
            prev = A
	    itr = A
	    set =0
        while itr.next:
            if itr.next.val<B and set:
                
                temp = itr.next.next
                itr.next.next= prev.next
                prev.next = itr.next
                itr.next =temp
            if itr.next.val<B and not set:
                itr = itr.next
                
            else:
                set=1
                itr = itr.next
        if prev.val ==None:
            return prev.next
        else:
            return prev
	            
