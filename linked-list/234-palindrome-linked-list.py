# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #fastest solution afaik
        if head.next == None: return True
        
        first_half = []
        fast = head
        slow = head
        while fast != None and fast.next != None:
            first_half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        #skip middle element if list length is odd
        if fast != None: slow = slow.next
        while slow != None:
            if slow.val != first_half.pop(): return False
            slow = slow.next
        return True
        
        
        '''
        #simpler solution
        if head.next == None: return True
        
        linked_list = []
        while head != None:
            linked_list.append(head.val)
            head = head.next
        return linked_list == linked_list[::-1]
        '''
        
        
        '''
        #fast and slow pointers
        if head.next == None: return True
        fast = head
        slow = head
        first_half = []
        second_half = []
        while fast != None and fast.next != None:
            first_half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        while slow != None:
            second_half.append(slow.val)
            slow = slow.next
        if len(second_half) > len(first_half):
            first_half.append(second_half[0])
        return first_half == second_half[::-1]
        '''