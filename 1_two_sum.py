import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seenValues = {}  # y => idx
        for idx, x in enumerate(nums):
            y = target - x
            if y in seenValues:
                return [seenValues[y], idx]
            seenValues[x] = idx
        return None


class TestSolution(unittest.TestCase):

    def test_unique_1(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_unique_2(self):
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])

    def test_repeated(self):
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])

    def test_no_result(self):
        self.assertIsNone(Solution().twoSum([3, 4], 6))


if __name__ == '__main__':
    unittest.main()
