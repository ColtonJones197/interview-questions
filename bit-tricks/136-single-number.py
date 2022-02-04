# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #crazy XOR solution
        number_to_flip = 0
        for num in nums:
            number_to_flip ^= num
        return number_to_flip