"""
740. Delete and Earn
Medium
6.3K
326
Companies
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.



Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
"""
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Top down DP using memoization and recursion
        def Max_Points(nums, i, memo):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            # Skip
            skip = Max_Points(nums, i + 1, memo)
            # Take
            take = nums[i][1] + Max_Points(nums, i + 2, memo)
            memo[i] = max(skip, take)
            return memo[i]

        if not nums:
            # case 1: empty list
            return 0
        if len(nums) == 1:
            # case 2: non-empty list
            return nums[0]
        if len(nums) == 2:
            # case 3: non-empty list
            return max(nums[0], nums[1])
        # case 4: non-empty list
        nums = sorted([(i, nums.count(i) * i) for i in set(nums)])
        return Max_Points(nums, 0, {})


