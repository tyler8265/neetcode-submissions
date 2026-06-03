class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, max_profit, cur_profit = 0, 0, 0 
        for right in range(len(prices)):
            cur_profit = prices[right] - prices[left]
            if cur_profit < 0:
                left = right
            else:
                max_profit = max(max_profit, cur_profit)
        return max_profit