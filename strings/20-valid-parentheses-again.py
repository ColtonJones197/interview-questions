# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        # could just use a hashmap for valid solutions
        def check(left, right):
            match(left):
                case '(': return right == ')'
                case '[': return right == ']'
                case '{': return right == '}'
            return None
        rights = (')', ']', '}')
        left_stack = []
        for char in s:
            if char in rights:
                if len(left_stack) == 0: return False
                if not check(left_stack.pop(), char): return False
            else: left_stack.append(char) # otherwise it's a right parenthese
        return len(left_stack) == 0