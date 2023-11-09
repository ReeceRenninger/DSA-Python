# [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Thought Process

    Initialize two pointers, left and right. left points to the index of buying, and right points to the index of selling. We start at the first and second indices, respectively, to consider the first two days.

    Initialize maxProfit to 0. This variable will keep track of the highest profit found.

    Enter a loop that iterates through the prices array while right is less than the length of the array. The loop will examine each day's stock price.

    Inside the loop, it checks if it's profitable to buy at the price pointed to by left and sell at the price pointed to by right. If the condition is met (prices are increasing), it calculates the profit by subtracting the buy price from the sell price.

    It then updates maxProfit to be the maximum of the current maxProfit and the profit calculated in this step. This step ensures that maxProfit always holds the highest profit found so far.

    If it's not profitable to buy at the current left index, it updates left to be the same as right. This move effectively considers the current day as a new buying day.

    Finally, it increments right to move to the next day and continues the loop.

    After the loop completes, it returns maxProfit, which holds the highest profit that could be obtained by buying and selling within the given price array.