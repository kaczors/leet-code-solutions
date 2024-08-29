# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

import unittest


class Solution(object):
    def isValid(self, s):
        mapping = {
          "{": "}",
          "(": ")",
          "[": "]"
        }
        buffer = ""
        for idx, c in enumerate(s):
          if c in mapping.keys():
            buffer += c
          else:
            if len(buffer) == 0 or mapping[buffer[-1]] != c:
              return False
            buffer = buffer[:-1]
        return len(buffer) == 0


class SolutionTestCase(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(Solution().isValid("()"), True)
        self.assertEqual(Solution().isValid("()[]{}"), True)
        self.assertEqual(Solution().isValid("([])"), True)

    def test_not_valid(self):
        self.assertEqual(Solution().isValid("(]"), False)


unittest.main()