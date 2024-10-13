# BRUTE FORCE
## use nested loops to iterate over all possible pairs of indices in array, check of numbers at indices to match target, if it does return the indices of the pair

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # set the length of nums to variable
        num_length = len(nums)
      # iterate through nums using i 
        for i in range(num_length):
            # inner loop i + 1 is setting j starting location, nums_length is what it will iterate over
            for j in range(i + 1, nums_length):
                # if the two indexed positions = target than we return the indexes
                if nums[i] + nums[j] == target:
                    return [i, j]
                

## IMPROVED
# One pass hash table, set up a dictionary and a variable to hold the length of nums, iterate over range of variable and generate the complement 
# variable using the target - nums[i] position, if that complement is in the dictionary(numMap) we want to return the indices so we dig into the 
# hash map with numMap[complement] and use i as the index pair, line 23 is mapping from each number in nums list to its index in the list and being 
# stored in numMap which is used to look up the index of a numbers complement when searching for pairs to hit target value

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            # storing nums[i] in dictionary using i as key
            numMap[nums[i]] = i

        return []  # No solution found