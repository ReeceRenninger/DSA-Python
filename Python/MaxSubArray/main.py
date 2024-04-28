class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        runningTotal = nums[0] #initalize value at nums[0] index position
        maxSum = nums[0] #initalize value at nums[0] index position

        for num in nums[1:]: # for loop starting at index 1 position since we set runningTotal and maxSum as start of nums
            runningTotal = max(num, runningTotal + num) #use max to grab either the largest num or total of runningTotal + num
            maxSum = max(maxSum, runningTotal) # use max to assign maxSum or runningTotal depending on which is larger
        return maxSum