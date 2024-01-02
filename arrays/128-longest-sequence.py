# https://leetcode.com/problems/longest-consecutive-sequence/description
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # could also use a dictionary
        longest_set = 0
        for num in nums:
            if num - 1 not in num_set: # Only look at values that could start a sequence
                length = 1
                while num + length in num_set: length += 1
                longest_set = max(length, longest_set)
        return longest_set
