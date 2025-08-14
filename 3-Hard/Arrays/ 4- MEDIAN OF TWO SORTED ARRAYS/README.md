# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We need to find the median of two sorted arrays. The median is the middle element when all elements are in order (or the average of the two middle elements if the total number of elements is even). A straightforward way is to merge both arrays into one sorted array and then pick the middle element(s).

---
# Problem Statement 
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

**Example 1:**

- Input: nums1 = [1,3], nums2 = [2]
- Output: 2.00000
- Explanation: merged array = [1,2,3] and median is 2.

**Example 2:**

- Input: nums1 = [1,2], nums2 = [3,4]
- Output: 2.50000
- Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

### Constraints:

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `106 <= nums1[i], nums2[i] <= 106`
  
---
# Approach
<!-- Describe your approach to solving the problem. -->
1. Merge the two arrays using concatenation: nums1 + nums2.
2. Sort the merged array in ascending order.
3. Determine the total length `n` of the merged array.
4. If `n` is odd, the median is the middle element at index n // 2.
5. If `n` is even, the median is the average of the two middle elements: mat indices n // 2 - 1 and n // 2.
6. Return the median as a float if it's an average, otherwise as the middle value.

---

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
![image.png](https://assets.leetcode.com/users/images/ddbf663b-fd8c-47c3-beeb-01574a9dc661_1755164424.7525127.png)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
![image.png](https://assets.leetcode.com/users/images/50bb7b15-62d9-4ef2-9680-274f1a09c8c7_1755164458.1194544.png)

# Code
```python []
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array =  nums1 + nums2
        merged_array.sort()
        n= len(merged_array)
        if  n % 2 == 1: 
            median = merged_array[n//2]
            return median 
        else: 
            median = (merged_array[n//2 -1] + merged_array[n//2]) / 2.0
            return median
```
