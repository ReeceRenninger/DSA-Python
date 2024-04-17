class Solution:
    # Sorted puts the letters into alphabetic order and then we do a comparison if all the same letters are present
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)