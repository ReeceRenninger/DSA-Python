from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # map character count to list of Anagram, have to use a defaultdict for KeyError issue

        for s in strs:
            count = [0] * 26 # represents whole alphabet

            for c in s:
                # use ord(a) as constant as we iterate through words in strs and increment by 1
                count[ord(c) - ord("a")] += 1
            # group counts that are equal
            result[tuple(count)].append(s)
        # return the results values from hashmap
        return result.values()