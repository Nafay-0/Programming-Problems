class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = n + m - 1
        while (1):
            if p1 < 0 or p2 < 0 or p < 0:
                break
            if nums2[p2] >= nums1[p1]:
                nums1[p] = nums2[p2]
                p2 = p2 - 1
                p = p - 1
            elif nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 = p1 - 1
                p = p - 1

        while p1 >= 0:
            nums1[p] = nums1[p1]
            p1 = p1 - 1
            p = p - 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 = p2 - 1
            p = p - 1

