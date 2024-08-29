import unittest


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) == 0:
            return result

        if len(strs) == 1:
            return strs[0]

        if len(strs) == 2:
            str1 = strs[0]
            str2 = strs[1]
            for idx, c in enumerate(str1):
                if idx + 1 > len(str2):
                    return result
                if c == str2[idx]:
                    result += c
                else:
                    break
            return result

        for idx, str in enumerate(strs):
            if idx == 0:
                result = self.longestCommonPrefix([str, strs[1]])
            result = self.longestCommonPrefix([str, result])

        return result


class TestCase(unittest.TestCase):
    def test_should_detect_common_prefix(self):
        self.assertEqual(Solution().longestCommonPrefix(
            ["flower", "flow", "flight"]), "fl")
        self.assertEqual(Solution().longestCommonPrefix(["cir", "car"]), "c")

    def test_should_return_empty_string_when_no_prefix(self):
        self.assertEqual(Solution().longestCommonPrefix(
            ["dog", "racecar", "car"]), "")


unittest.main()
