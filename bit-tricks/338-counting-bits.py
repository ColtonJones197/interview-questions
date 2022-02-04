# https://leetcode.com/problems/counting-bits/
import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        one_counts = []
        for num in range(0, n + 1):
            #find the number of one's LMAO
            val = num
            count = 1
            if val < 2:
                one_counts.append(val)
            else:
                while val > 1:
                    count += val % 2
                    val >>= 1
                one_counts.append(count)
        return one_counts