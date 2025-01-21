class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        count = 0
        for i in range(0, len(nums)):
            if count == 0:
                # selecting new candidate for majority element
                candidate = nums[i]
                count += 1
            # if match, increment count by 1
            elif nums[i] == candidate:
                count += 1
            else:
                count -= 1

        return candidate
