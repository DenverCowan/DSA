'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.'''
List = [7,1,5,3,6,4] # sample case

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum_price = float("inf") # sets the min value to infinity 
        max_profit = 0

        for price in prices: # iterate through the list
            
            if price < minimum_price: # set min price to lowest price in the list
                minimum_price = price
                
            if price - minimum_price > max_profit: # set max profit to current highest price - minimum price
                max_profit = price - minimum_price
                
        return max_profit # return max profit
        '''Solution is O(n) with n being the size of the list.'''