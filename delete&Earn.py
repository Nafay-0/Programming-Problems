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
    def deleteAndEarn(self,nums):
        nums.sort()  # Sort the input list
        # Initialize dp array with -1
        dp = [-1] * (len(nums) + 1)
        # Top down recursive function
        def Max_points(nums, i):
            if i >= len(nums):
                return 0

            if dp[i] != -1:
                return dp[i]
            # Initialize add and d
            add = 0
            d = 0
            pos = -1
            # Iterate through the list
            for j in range(i, len(nums)):
                # If the current element is equal to the next element
                if nums[i] == nums[j]:
                    d += 1
                # If the current element is equal to the next element + 1
                elif nums[i] + 1 == nums[j]:
                    pos = j
                else:
                    break
            # Add the current element to the add variable
            add += (d * nums[i])
            # If the position is not -1
            if pos != -1:
                # Set the dp array to the maximum of the recursive call of the current element + 1 and the recursive call of the position + 1
                dp[i] = max(Max_points(nums, pos + 1) + add, Max_points(nums, i + 1))
            else:
                # Set the dp array to the recursive call of the current element + 1
                dp[i] = max(Max_points(nums, i + d) + add, Max_points(nums, i + d))
                # Return the dp array
            return dp[i]

        return Max_points(nums, 0)


