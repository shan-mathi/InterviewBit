# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A is None or A.next is None:
            return A
        temp = ListNode(-1)
        temp.next = A
        
        current = temp
        while current.next is not None and current.next.next is not None:
            first = current.next
            second = current.next.next
            first.next = second.next
            current.next = second
            current.next.next = first
            current = current.next.next
        return temp.next
