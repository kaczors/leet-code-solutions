# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers, return the number with the largest value.

import unittest


class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        distance = None
        for x in nums:
            dis = abs(x)
            if result == None or distance > dis or (distance == dis and x > result):
                result = x
                distance = dis
        return result


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(Solution().findClosestNumber([-4, -2, 1, 4, 8]), 1)
        self.assertEqual(Solution().findClosestNumber([2, -1, 1]), 1)
        self.assertEqual(Solution().findClosestNumber([0, 1]), 0)


unittest.main()
