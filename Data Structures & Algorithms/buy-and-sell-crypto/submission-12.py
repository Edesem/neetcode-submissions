class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 0
        profit = 0

        while r < n - 1:
            print(prices[l], prices[r])
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
            profit = max(profit, prices[r] - prices[l])

        return profit
