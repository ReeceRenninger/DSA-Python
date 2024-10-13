# [LeetCode 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## Thought Process

Had no idea on how to approach this problem upon reading the description.

Read some comments that talked about Kadane's algorithm as the way to getting to solution.

Read through Kadane's algorithm and helped it to guide me on how I should set up my code.

Started out my initializing a variable called `maxSum` and set it to the first index position in the array.

Then, I created a for loop that would iterate through the array, starting at the second index position.

Inside the for loop, I created a variable called `nums[i]` and set it to the value of the current index position.

`Math.max(0, nums[i-1] + nums[i])` computes the maximum between 0 and the sum of the previous nums[i-1] and the current element nums[i]. This is crucial because if adding the current element to the previous subarray sum results in a smaller value than the current element itself, it's better to start a new subarray from the current element. The value assigned to nums[i] is the maximum of these two options.

Then, I created an if statement that would check if the `nums[i]` was greater than the `maxSum`, if it was, I would set the `maxSum` to the `nums[i]`.

Then, I created another for loop that would iterate through the array, starting at the second index position.