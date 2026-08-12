class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                ans = max(prices[r]-prices[l], ans)
            r+=1
        return ans



