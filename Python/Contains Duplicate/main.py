# approach was to create a duplicate set and iterate over the array and if a number was already present in the set then we return True otherwise continue to add number to the set, if completed we return False
## This should have a time of O(n) and n being the length of the array

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # create a set, as we iterate we add each element, since set only takes unique
         # if an element tries to be added but exists already we retrun true if we
         # make it to the end of the array we return false
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

