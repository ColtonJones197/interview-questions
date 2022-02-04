# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = nums[0]
        best_sum_here = -10 ** 4
        for i in range(0, len(nums)):
            best_sum_here = max(best_sum_here + nums[i], nums[i])
            best_sum = max(best_sum, best_sum_here)
        return best_sum