# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        def getCombinations(self, digits: str) -> List[str]:
            if digits == '': return []
            results = []
            letters = self.phone[digits[0]]
            for letter in letters:
                if len(digits) == 1:
                    results.append(letter)
                else:
                    combinations = getCombinations(self, digits[1:])
                    for comb in combinations:
                        results.append(letter + comb)
            return results
        return getCombinations(self, digits)