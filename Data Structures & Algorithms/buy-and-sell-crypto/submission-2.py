class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] > prices[r]:
                if l+1 == r:
                    l+=1
                    r+=1
                else:
                    l+=1
                continue
            ans = max(prices[r]-prices[l], ans)
            r+=1
        return ans



