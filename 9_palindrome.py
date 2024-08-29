import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_as_string = str(x)
        x_as_string_revered = ''
        for idx, c in enumerate(x_as_string):
            x_as_string_revered += x_as_string[len(x_as_string) - idx - 1]
        return x_as_string == x_as_string_revered

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_as_string = str(x)
        return x_as_string == x_as_string[::-1]

    def isPalindrome3(self, x):
        num = x
        result = 1  # init with 1 just to enter the loop
        reminder = 0  # div rest
        y = 0 # reversed
        if x < 0:
            return False
        while result > 0:
            reminder = num % 10
            result = num // 10
            num = result
            if y != 0:
              y = y * 10
            y = y + reminder
        return x == y      
            
            
                  
          
          

        


class TestSolution(unittest.TestCase):

    def test_poisitive_number_palindrome(self):
        self.assertTrue(Solution().isPalindrome(121))
        self.assertTrue(Solution().isPalindrome2(121))
        self.assertTrue(Solution().isPalindrome3(121))

    def test_poisitive_number_not_palindrome(self):
        self.assertFalse(Solution().isPalindrome(10))
        self.assertFalse(Solution().isPalindrome2(10))
        self.assertFalse(Solution().isPalindrome3(10))

    def test_negative_number_palindrome(self):
        self.assertFalse(Solution().isPalindrome(-121))
        self.assertFalse(Solution().isPalindrome2(-121))
        self.assertFalse(Solution().isPalindrome3(-121))


if __name__ == '__main__':
    unittest.main()
