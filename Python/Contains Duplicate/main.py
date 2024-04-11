# approach was to create a duplicate set and iterate over the array and if a number was already present in the set then we return True otherwise continue to add number to the set, if completed we return False
## This should have a time of O(n) and n being the length of the array

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for number in nums:
            if number in duplicate:
                return True
            duplicate.add(number)
        return False

