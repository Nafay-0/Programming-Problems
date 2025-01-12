"""
59. Spiral Matrix II
Medium
5.7K
234
Companies
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
Accepted
497.4K
Submissions
713.8K
Acceptance Rate
69.7%
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        matrix = [[0 for i in range(n)] for j in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left-1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix