# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prof = 10 ** 4
        max_prof = 0
        for index in range(0, len(prices)):
            if prices[index] < min_prof:
                min_prof = prices[index]
            else:
                max_prof = max(max_prof, prices[index] - min_prof)
        return max_prof