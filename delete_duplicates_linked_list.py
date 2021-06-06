# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        prev_prev = None
        prev = A
        current = A.next
    
        while current:
            if current.val != prev.val:
                prev_prev = prev
                prev = current
                current = current.next
            else:
                while current  and current.val == prev.val:
                    prev = current
                    current = current.next
                if prev_prev != None: prev_prev.next = current
                if prev_prev == None: A = current
                prev = current
                if current: current = current.next
        return A
        
def delete_duplicate_my_solution(A):
    clock = None
    itr = A
    prev = None
    while itr:
        if clock and itr.val == clock:
            if prev:
                prev.next = itr.next
            itr = itr.next
            if itr == None:
                return A

        elif itr.next == None:
            return A


        elif itr.val != itr.next.val:
            if prev == None:
                A = itr
            prev = itr
            clock = None
            itr = itr.next
        elif itr.val == itr.next.val:

            clock = itr.val
            if prev:
                prev.next = itr.next
            itr = itr.next        
