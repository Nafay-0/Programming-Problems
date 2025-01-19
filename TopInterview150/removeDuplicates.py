class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_index = 1
        unique_index = 0

        while start_index < len(nums):
            if nums[start_index] != nums[unique_index]:
                nums[unique_index + 1] = nums[start_index]
                unique_index += 1
            start_index += 1
        return unique_index + 1

