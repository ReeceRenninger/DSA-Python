class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) #initialize the length of input array
        
        prefix = [1] * n # initialize with 1 and length of input array
        suffix = [1] * n # initialize with 1 and length of input array
        
        #calculate the prefix products, start at index 1 and goes up to n-a
        # for each index of i prefix[i] is assigned the product of all elements BEFORE nums[i]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # calculate the suffix products, loop starts from the second to last index(n - 2) and goes backward down to 0
        # each index i, suffix[i] is assigned the product of all elements AFTER nums[i]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # multiply the prefix and suffix products for each index, by iterating over each index i and 
        # calculating prefix[i] *suffix[i]
        answer = [prefix[i] * suffix[i] for i in range(n)]
        
        return answer