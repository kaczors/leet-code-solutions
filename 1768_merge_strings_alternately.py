import unittest

# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if not word1 and not word2:
            return ""
        if not word2:
            return word1
        if not word1:
            return word2

        result = ""

        for idx, c1 in enumerate(word1):
            if idx == len(word2):
                return result + word1[idx:]
            result += c1
            result += word2[idx]

        if len(word2) > len(word1):
            return result + word2[idx+1:]
        return result


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(Solution().mergeAlternately("a", ""), "a")
        self.assertEqual(Solution().mergeAlternately("a", None), "a")
        self.assertEqual(Solution().mergeAlternately("a", "b"), "ab")
        self.assertEqual(Solution().mergeAlternately("abc", "pqr"), "apbqcr")
        self.assertEqual(Solution().mergeAlternately("ab", "pqrs"), "apbqrs")
        self.assertEqual(Solution().mergeAlternately("abcd", "pq"), "apbqcd")


unittest.main()
