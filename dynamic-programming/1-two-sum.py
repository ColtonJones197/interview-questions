# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap solution
        hasher = {}
        for i in range(0, len(nums)):
            if hasher.get(nums[i]) != None:
                return [hasher.get(nums[i]), i]
            hasher[target - nums[i]] = i
                
        
        
        '''for i in range(0, len(nums)):
            x = nums[i]
            for k in range(i + 1, len(nums)):
                if x + nums[k] == target:
                    return [i, k]'''