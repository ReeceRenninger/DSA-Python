class Solution:
    # Sorted puts the letters into alphabetic order and then we do a comparison if all the same letters are present
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # BONUS CHALLENGE: how would you solve this if you were given non UNICODE characters? or strings with varying capitlization?
    def isAnagram(self, s: str, t: str) -> bool:
        s_normal = s.lower()
        t_normal = t.lower()

        # create a custom sort function to group the alphanumeric and non - alphanumeric for comparison later
        def custom_sorter(string):
            #sorted by default sorts by the natural order, so alphanumeric before non
            # we pass the string s and t while using the lambda function as a key the lambda function takes each character x and returns a tupe of (x.isalnum(), x)
            # x.isalnum() returns true if alphanumeric(letter or digit) and False otherwise
            return sorted(string, key=lambda x: (x.isalnum(), x))
        
        # run the sorted strings through the customer sorter then do a return comparator if equal to return True or False otherwise
        sorted_s = custom_sorter(s_normal)
        sorted_t = custom_sorter(t_normal)

        return sorted_s == sorted_t