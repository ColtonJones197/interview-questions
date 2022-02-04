# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_hash = {}
        for num in nums:
            num_hash[num] = ''
        missing_nums = []
        for num in range(1, len(nums) + 1):
            if num_hash.get(num) == None:
                missing_nums.append(num)
        return missing_nums