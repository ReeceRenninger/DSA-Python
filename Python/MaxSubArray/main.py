class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        runningTotal = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            runningTotal = max(num, runningTotal + num)
            maxSum = max(maxSum, runningTotal)
        return maxSum