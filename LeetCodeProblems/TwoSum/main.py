class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
   
        # dictionaries are similar to how we can set up hashmap in JS
        sum_map = {}
        
        # need to iterate and enumerate the nums to get index
        # enumerate returns a tuple of index and value
        # i is the index and num is the value
        for i, num in enumerate(nums):
            # the complement is the difference between target and num
            complement = target - num

            # looking for pair that adds up
            if complement in sum_map:
                # returns the complement stored and the i that added to target
                return [sum_map[complement], i]
            
            # this will store the num as the key and the index as the value
            sum_map[num] = i
        #no solution
        return []