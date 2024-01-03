# https://leetcode.com/problems/generate-parentheses/description/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Making decisions so we'll be using backtrackign
        # also need to keep track of all values

        # closures
        stack = []
        res = []

        # backtrack method
        def generate_valid_combs(num_open, num_closed) -> List[str]:
            if num_open == n and num_closed == n:
                res.append("".join(stack))
                return
            if num_open < n:
                stack.append("(")
                generate_valid_combs(num_open + 1, num_closed)
                stack.pop()
            if num_closed < num_open:
                stack.append(")")
                generate_valid_combs(num_open, num_closed + 1)
                stack.pop()
        generate_valid_combs(0, 0)
        return res
