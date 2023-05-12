"""
47. Permutations II
Medium
7.4K
130
Companies
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n!)
        Space complexity: O(n!)
        """
        n = len(nums)
        output = []
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                if i > first and nums[i] == nums[first]:
                    continue
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        backtrack()
        return output

