# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
 The problem asks for two numbers that add up to a target value. Instead of checking every possible pair (which is slow), we can store the numbers we’ve already seen in a dictionary for quick lookups. This way, as we go through the list, we can instantly check if the
complement of the current number has been seen before.



## Problem Statement

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

You may assume that:
- Each input will have exactly **one** solution.
- You may not use the same element twice.
- The answer can be returned in any order.

---

### Examples

**Example 1**

 - Input: nums = [2,7,11,15], target = 9
 
 - Output: [0,1]
 
 - Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2**

 - Input: nums = [3,2,4], target = 6
 
 - Output: [1,2]

**Example 3**

 - Input: nums = [3,3], target = 6
 
 - Output: [0,1]
  
### Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only **one valid answer** exists.

---

### Follow-up
Can you design an algorithm with time complexity **better than O(n²)**?

---

# Approach
<!-- Describe your approach to solving the problem. -->
1. Create an empty dictionary to map numbers to their indices.
2. Iterate through the list using enumerate() to get both index and value.
3. For each number, calculate the complement (target - current number).
4. If the complement is already in the dictionary, return the stored index along with the current index (solution found).
5. Otherwise, store the current number and its index in the dictionary.
6. This ensures each number is processed once, giving O(n) time complexity.

# Complexity

<!-- Add your time complexity here, e.g. $$O(n)$$ -->
![image.png](https://assets.leetcode.com/users/images/0074f5c0-dfe5-4c98-b0a4-677ee18d6281_1755162810.4200497.png)

![image.png](https://assets.leetcode.com/users/images/16ab26ab-f81f-479d-b710-efdac8ba1832_1755162848.5832148.png)

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python []
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

```
