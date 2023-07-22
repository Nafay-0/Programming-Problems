"""
93. Restore IP Addresses
Medium
4.8K
757
Companies
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Constraints:

1 <= s.length <= 20
s consists of digits only.
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Backtracking
        def valid(s):
            if len(s) > 1 and s[0] == '0':
                return False
            return int(s) <= 255
        def backtrack(s, path, res):
            if len(path) == 4:
                if not s:
                    res.append('.'.join(path))
                return
            for i in range(1, 4):
                if i > len(s):
                    break
                if valid(s[:i]):
                    backtrack(s[i:], path+[s[:i]], res)
        res = []
        backtrack(s, [], res)
        return res
