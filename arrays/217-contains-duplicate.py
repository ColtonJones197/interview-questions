# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_hash = {}
        for num in nums:
            if num_hash.get(num) != None: return True
            num_hash[num] = ''
        return False