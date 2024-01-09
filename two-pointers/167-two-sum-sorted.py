# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            cur_sum = numbers[start] + numbers[end]
            if cur_sum < target:
                start += 1
            elif cur_sum > target:
                end -= 1
            else:
                return [start + 1, end + 1]