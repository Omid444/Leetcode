class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == "-":
            reverse_x = -int(s[:0:-1])

        else:
            reverse_x = -int(s[:0:-1])

        if reverse_x < -2**31 or reverse_x > 2**31 - 1:
            return 0

        return reverse_x



s = Solution()
print(s.reverse(-123))