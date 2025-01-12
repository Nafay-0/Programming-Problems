"""
7. Reverse Integer
Medium
9.7K
11.6K
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = int(str(x)[1:][::-1]) * -1
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        return x
