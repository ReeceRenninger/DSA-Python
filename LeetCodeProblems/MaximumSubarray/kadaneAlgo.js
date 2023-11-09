/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  // we need to initalize a max sum variable
  let maxSum = nums[0];
  // traverse all the elements given in the array with a loop
  for(let i = 1; i < nums.length; i++){
      // used Kadane algo for the logic creation
      // nums[i] will present the largest sum of all subarrays ending with index i
      // its values should be the larger one between nums[i]
      // the nums[i-1] + nums[i] should be the largest sum plus current number with using the prefix
      // will calculate nums[0], nums[1] and continuing forward through the entire length while comparing each one against the largest sum, maxSum
      nums[i] = Math.max(0, nums[i-1] + nums[i]);
      //if our nums[i] > maxSum then reassign maxSum = nums[i]
      if(nums[i] > maxSum)
          maxSum = nums[i];
  }
  return maxSum; //return the subarray which has the largest sum
};