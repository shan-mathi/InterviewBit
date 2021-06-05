# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        prev = None
        itr = A
        while itr:
            nextt = itr.next
            itr.next = prev
            prev = itr
            itr = nextt
        A = prev
        return A

            
            
