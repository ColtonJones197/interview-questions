# https://leetcode.com/problems/binary-search/submissions/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(array, element, start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if element == array[mid]:
                return mid
            if element < array[mid]:
                return bst(array, element, start, mid - 1)
            if element > array[mid]:
                return bst(array, element, mid + 1, end)
        
        return bst(nums, target, 0, len(nums) - 1)