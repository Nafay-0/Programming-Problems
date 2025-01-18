class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ind = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind = ind + 1

        return ind