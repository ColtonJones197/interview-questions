# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #faster linked list traversal
        try:
            slow = head
            fast = head
            while True:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    return True
        except AttributeError:
            return False
        
        
        
        
        '''if type(head) == type(None): return False
        val_hash = {}
        while head.next != None:
            if val_hash.get(head) != None:
                return True
            val_hash[head] = ''
            head = head.next
            
        return False'''