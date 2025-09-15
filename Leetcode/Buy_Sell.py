class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)
        return max_profit

# Runtime - O(n)
# Space - O(1)



"""
prices is arrray
prices[i] = price of stock on day i, [7,1,4,5]- price is 7 on day 1 and 1 on day 2
need a profit return
0 if no profit
buy day
sell day

class Solution:
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       max_profit = 0
       n = len(prices)
       for i in range(n):             # buy day
             for j in range(i+1, n):    # sell day (must be after buy)
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
       return max_profit

Runtime: O(n^2)
Space: O(1)

"""