'''
Leetcode- 122. Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Time complexity - O(N)
Space complexity - O(1)
Approach - We need to find the peak and valleys in an given array

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0: return 0
        i=0
        peak=prices[0]
        valley=prices[0]
        maxprofit=0
        while i<len(prices)-1:
            while i<len(prices)-1 and prices[i]>=prices[i+1]:
                i=i+1
            valley=prices[i]
            
            while i<len(prices)-1 and prices[i]<=prices[i+1]:
                i=i+1
            peak=prices[i]
            maxprofit+= peak-valley
        return maxprofit