# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = []
        prefix, postfix = 1, 1
        
        for num in nums:
            answers.append(prefix)
            prefix = prefix * num

        # go backwards through the array and multiply in place
        for index in range(len(nums)-1, -1, -1):
            answers[index] = answers[index] * postfix
            postfix = postfix * nums[index] #note that I'm still using numbs here
        
        return answers