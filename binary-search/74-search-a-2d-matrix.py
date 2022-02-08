# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchLine(line: List[int], target, start, end) -> bool:
            if start > end:
                return False
            mid = (start + end) // 2
            if line[mid] == target:
                return True
            if line[mid] > target:
                return searchLine(line, target, start, mid - 1)
            if line[mid] < target:
                return searchLine(line, target, mid + 1, end)
            
        def searchRows(matrix: List[List[int]], target, start, end) -> bool:
            if start > end:
                return False
            mid = (start + end) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return searchLine(matrix[mid], target, 0, len(matrix[mid]) - 1)
            if matrix[mid][-1] > target:
                return searchRows(matrix, target, start, mid - 1)
            if matrix[mid][0] < target:
                return searchRows(matrix, target, mid + 1, end)
        return searchRows(matrix, target, 0, len(matrix) - 1)