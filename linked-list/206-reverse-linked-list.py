# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        curr = head
        prev = None
        nextNode = head.next
        while curr != None:
            curr.next = prev
            prev = curr
            curr = nextNode
            if nextNode != None: nextNode = nextNode.next
        
        return prev