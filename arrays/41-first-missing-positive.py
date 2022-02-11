# https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # actual solution, had to look this up because it's not intuitive at all.
        # interesting though
        # runs in O(3n) -> O(n) time, and uses constant space because we modify the input in place
        
        #1st pass, 0 out all numbers that we don't care about (in place to save space)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = (len(nums) + 1) * -1
                    
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1
        
        '''
        # O(n) space, O(n) time
        hash_set = {}
        for num in nums:
            hash_set[num] = num
        for i in range (1, len(nums) + 1):
            if hash_set.get(i) == None:
                return i
        return len(nums) + 1'''
        
        '''
        # O(n) space, O(nlogn) time
        smallest = 1
        sorted_arr = nums.copy()
        sorted_arr.sort()
        for num in sorted_arr:
            if num > 0 and smallest == num:
                smallest += 1
        return smallest'''