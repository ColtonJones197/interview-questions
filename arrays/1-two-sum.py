# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # So here, I can use a dictionary to store the differences at each list as I iterate through the list
        # if target - the value that I'm currently on exists in keys, return the index that I'm currently on and the value at target - current val
        # so k: index of the element, v: target - value at element
        diffToIndexMap = {}
        for index in range(0, len(nums)):
            currentVal = nums[index]
            diff = target - currentVal
            if diff in diffToIndexMap.keys():
                # we have our solution
                return [diffToIndexMap[diff], index]
            diffToIndexMap[currentVal] = index