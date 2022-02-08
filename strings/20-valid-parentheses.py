# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        for paren in s:
            if paren in mappings.keys():
                stack.append(paren)
            else:
                if len(stack) == 0:
                    return False
                left_paren = stack.pop()
                if mappings.get(left_paren) != paren:
                    return False
        return len(stack) == 0