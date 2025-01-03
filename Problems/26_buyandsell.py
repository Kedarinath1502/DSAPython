'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing
 a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution(object):
    def maxProfit(self, prices):
        l , r = 0, 1
        maxi = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxi = max(maxi, prices[r] - prices[l])
            else:
                l = r
            r = r + 1
        return maxi