"""Description:
You are given an array prices where prices[i] is the price of a stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell it.
Return the maximum profit you can achieve. If you can't make any profit, return 0.

"""

"""Input: prices = [7,1,5,3,6,4]  
Output: 5  
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5
"""

def maxProfit(prices):
    min_price = float('inf')  # Initialize min_price to infinity
    max_profit = 0  # Initialize max_profit to 0

    for price in prices:
        if price < min_price:
            min_price = price

        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit
 
price = [7,1,5,3,6,4]
print(maxProfit(price))  