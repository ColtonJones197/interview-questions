# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        pointer = head
        while pointer.next != None:
            if pointer.next.val == pointer.val:
                pointer.next = pointer.next.next
            else: pointer = pointer.next
        return head