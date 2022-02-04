# https://leetcode.com/problems/climbing-stairs/submissions/
class Solution:
    def climbStairs(self, n: int) -> int:
        #This was my first time attempting to solve a dynamic programming problem
        #I eventually realized this just follows the fibonacci sequence.
        def fibonacci(x: int, y: int, iterations: int) -> int:
            if iterations == 0:
                return x
            return fibonacci(y, x + y, iterations - 1)
        return fibonacci(1,1,n)
    