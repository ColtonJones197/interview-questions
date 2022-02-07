# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        successes = []
        
        def backtrack(i, current, target):
            if target < 0 or i == len(candidates):
                return
            if target == 0:
                successes.append(current.copy())
                return
            current.append(candidates[i])
            backtrack(i, current, target - candidates[i])
            current.pop()
            backtrack(i + 1, current, target)
            
        backtrack(0, [], target)
        return successes