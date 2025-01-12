"""
5. Longest Palindromic Substring
Medium
Companies
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_palindrome = ""
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrome = s[i]
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest_palindrome = s[i:i + 2]
        for i in range(len(s) - 3, -1, -1):
            for j in range(i + 2, len(s)):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > len(longest_palindrome):
                        longest_palindrome = s[i:j + 1]
        return longest_palindrome
