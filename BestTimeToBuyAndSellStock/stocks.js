'use strict';

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  // use a 2 pointer method
  let left = 0; //buy pointer starting at first index
  let right = 1; //sell pointer starting at second index
  let maxProfit = 0 //our variable to hold our highest price

  while(right < prices.length){
      if(prices[left] < prices[right]){ // 
          let profit = prices[right] - prices[left]; // our current profit

          maxProfit = Math.max(maxProfit, profit); // calculate the maxProfit to profit variable
      } else {
          left = right; // move the pointer of left to the right
      }
      right++; //move the right pointer over
  }
  return maxProfit; // return the maxProfit variable
};