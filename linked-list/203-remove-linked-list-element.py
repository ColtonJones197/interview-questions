# https://leetcode.com/problems/remove-linked-list-elements/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head != None and head.val == val:
            head = head.next
        if head == None: return head
        prev = head
        pointer = head.next
        while pointer != None:
            if pointer.val == val:
                prev.next = pointer.next
                pointer = pointer.next
            else:
                prev = pointer
                pointer = pointer.next
        return head