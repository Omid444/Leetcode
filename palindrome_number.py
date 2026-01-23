class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        up_to_middle = 0
        while x > up_to_middle:
            up_to_middle = up_to_middle * 10 + x % 10
            x //= 10

        return x == up_to_middle or x == up_to_middle // 10


s = Solution()

print(s.isPalindrome(121))