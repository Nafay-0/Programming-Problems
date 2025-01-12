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


def distance(x): # calculate the distance from the origin
    return x[0] * x[0] + x[1] * x[1]


def helper(nums, K): # find the K closest points
    if len(nums) == 1:
        return nums
    n = len(nums) // 2
    # divide and conquer
    left_points = helper(nums[:n], K)
    right_points = helper(nums[n:], K)
    # merge
    res = []
    left = 0
    right = 0
    while K > 0 and left < len(left_points) and right < len(right_points):
        if distance(left_points[left]) <= distance(right_points[right]):
            res.append(left_points[left])
            left += 1
            K -= 1
        else:
            res.append(right_points[right])
            right += 1
            K -= 1
    while K > 0 and left < len(left_points):
        res.append(left_points[left])
        left += 1
        K -= 1
    while K > 0 and right < len(right_points):
        res.append(right_points[right])
        right += 1
        K -= 1
    return res


class Solution:
    def kClosest(self,points, K):
        return helper(points, K)
