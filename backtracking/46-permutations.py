# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(nums: List[int]) -> List[List[int]]:
            if len(nums) == 1: return [[*nums]]
            results = []
            for num in nums:
                remaining = [*nums]
                remaining.remove(num)
                perms = permutations(remaining)
                for perm in perms:
                    results.append([num, *perm])
            return results
        return permutations(nums)