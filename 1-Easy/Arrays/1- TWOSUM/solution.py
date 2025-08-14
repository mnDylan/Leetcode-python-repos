class Solution(object):
    def twoSum(self, nums, target):
    # Create a dictionary to store the value and its index
        num_map = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already in the map
            if complement in num_map:
                return [num_map[complement], i]  # Return the indices
            
            # Otherwise, add the current number to the map
            num_map[num] = i
