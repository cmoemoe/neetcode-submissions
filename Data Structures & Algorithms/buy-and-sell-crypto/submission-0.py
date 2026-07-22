class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        max_res = 0
        for sell in range(1, len(prices)):
            temp = prices[sell] - min(prices[:sell])
            if temp > max_res:
                max_res = temp

        return max_res