class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_=inf
        max_=0
        for i in range(len(prices)):
            if prices[i]<min_:
                min_=prices[i]
            elif prices[i]-min_>max_:
                max_=prices[i]-min_
        
        return max_