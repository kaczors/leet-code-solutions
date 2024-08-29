import unittest


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num = 0
        for idx, c in enumerate(s):
            if c == "I" and idx != (len(s) - 1) and s[idx + 1] in ["V", "X"]:
                continue

            if c == "X" and idx != (len(s) - 1) and s[idx + 1] in ["L", "C"]:
                continue

            if c == "C" and idx != (len(s) - 1) and s[idx + 1] in ["D", "M"]:
                continue

            substraction = 0
            if idx > 0 and c in ["V", "X"] and s[idx - 1] == "I":
                substraction = 1
            if idx > 0 and c in ["L", "C"] and s[idx - 1] == "X":
                substraction = 10
            if idx > 0 and c in ["D", "M"] and s[idx - 1] == "C":
                substraction = 100
            num += charMappings[c] - substraction
        return num


class TestSolution(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(Solution().romanToInt("III"), 3)
        self.assertEqual(Solution().romanToInt("IV"), 4)
        self.assertEqual(Solution().romanToInt("LVIII"), 58)
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)


unittest.main()
