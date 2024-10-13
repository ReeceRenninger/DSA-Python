class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #create a variable assigned to first value in prices
        min_price = prices[0]
        #create a variable starting at 0
        max_profit = 0
        
        # iterate through prices starting at the 2nd element,
        # because we set the min_price to the first element
        for price in prices[1:]:
            # reassign variable using max fucntion to test the potential
            # profit by selling at the current price and buying at min_price
            max_profit = max(max_profit, price - min_price)
            # updates min_price to the minimum of current min_price and price, 
            # this ensures min_price always represnets min price seen so far
            min_price = min(min_price, price)
        
        return max_profit
