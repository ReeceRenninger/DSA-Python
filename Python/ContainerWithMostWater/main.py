class Solution:
    def maxArea(self, height: List[int]) -> int:
       left = 0 # start at front of height
       right = len(height) - 1 # start at back of height
       maxArea = 0 # tracker for maxArea 

       # pointers work towards middle from each end, once left > right we've passed midpoint so loop ends
       while left < right:
            # use min function to find min height between left and right pointers, multiply this by difference b/w indices
            # of the pointers, store it as currentArea
            currentArea = min(height[left], height[right]) * (right - left)
            # max function to take the larger number between currentArea and maxArea
            maxArea = max(maxArea, currentArea)
            # check if left pointer is less than right and move it towards center
            if height[left] < height[right]:
                left += 1
            # otherwise move the right towards the center
            else:
                right -= 1
        # return the maxArea
       return maxArea