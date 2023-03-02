"""
973. K Closest Points to Origin
Medium
7.2K
259
Companies
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).



Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.


Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104
"""
class Solution(object):
    '''
    we use the divide and conquer method to find the kth largest number
    meanwhile due to the partition function
    after the kth number is found the points[0] to points[k-1] are all points are
    all answers
    '''

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        l = []
        ans = self.findkth(points, 0, len(points) - 1, K)
        for i in range(0, K, 1):
            l.append([])
            l[i].append(points[i][0])
            l[i].append(points[i][1])

        return l

    def findkth(self, points, low, high, k):
        pivot = self.partition(points, low, high)
        if pivot == k - 1:
            return points[k - 1]
        if pivot > k - 1:
            return self.findkth(points, low, pivot - 1, k)
        return self.findkth(points, pivot + 1, high, k)

    '''
	the partition function is the same as the quicksort with median of three partition function
	and return the pivot
	'''

    def partition(self, points, low, high):
        mid = self.mid3(points, low, high)
        self.swap(points, low, mid)
        key = points[low][0] * points[low][0] + points[low][1] * points[low][1]
        while (low < high):
            while (low < high and key <= points[high][0] * points[high][0] + points[high][1] * points[high][1]):
                high -= 1
            self.swap(points, low, high)

            while (low < high and key >= points[low][0] * points[low][0] + points[low][1] * points[low][1]):
                low += 1
            self.swap(points, low, high)
        return low

    def mid3(self, nums, low, high):
        mid = (low + high) // 2
        l = []
        l.append(nums[low])
        l.append(nums[mid])
        l.append(nums[high])
        l.sort()
        if l[1] == nums[low]:
            return low
        elif l[1] == nums[mid]:
            return mid
        return high

    def swap(self, nums, index1, index2):
        tmp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = tmp
        return