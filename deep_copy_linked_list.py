# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        
        #return head
        #copy list
        itr = head
        while itr:
            copy = RandomListNode(itr.label)
            temp = itr.next
            itr.next = copy
            copy.next = temp
            itr = temp
        
        itr = head
        while itr:
            itr.next.random = itr.random.next
            itr = itr.next.next
        #create copy list
        ans = head.next
        itr = ans
        while itr or itr.next.next:
            itr.next = itr.next.next
            itr = itr.next
        
        return ans

        
        
        
"""    def copy_list(self, head):
        itr = head
        c = RandomListNode(0)
        copy = c
        
        while itr:
            copy.label = itr.label
            copy.next = RandomListNode(0)
            itr = itr.next
            copy = copy.next
        return c"""
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
