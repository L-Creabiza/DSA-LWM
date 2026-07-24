class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cprofit = 0
        mprofit = 0
        minprice = prices[0]
        for i in range(len(prices)):
            if minprice > prices[i]:
                minprice = prices[i]
            cprofit = prices[i] - minprice
            mprofit = max(mprofit, cprofit)
        if mprofit < 0:
            return 0
        else:
            return mprofit