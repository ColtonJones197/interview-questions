# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(stack, operation):
            rhs = stack.pop()
            lhs = stack.pop()
            match operation:
                case "+":
                    return lhs + rhs
                case "-":
                    return lhs - rhs
                case "*":
                    return lhs * rhs
                case "/":
                    return int(float(lhs) / rhs)

        num_stack = []
        operations = ("+", "-", "*", "/")

        for token in tokens:
            if token in operations:
                num_stack.append(operate(num_stack, token))
            else:
                num_stack.append(int(token))

        return num_stack.pop()
        