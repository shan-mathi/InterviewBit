# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#using Floyd's technique

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        fp,sp = A,A
        s=0
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            
            if fp==sp:
                s=1
                break
        if not s:
            return None
        
        fp = A
        while fp!=sp:
            fp = fp.next
            sp = sp.next
            
        return fp
