class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit_list = []
        s = s.lstrip()
        if not s:
            return 0

        neg_or_pos = 1
        if s[0] in ["-","+"]:
            if s[0] == "-":
                neg_or_pos = -1
            s = s[1:]

        for char in s:
            if not char.isdigit():
                break
            else:
                digit_list.append(char)

        if not digit_list or digit_list == ["+"] or digit_list == ["-"]:
            return 0
        num = int("".join(digit_list)) * neg_or_pos

        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num

s = Solution()
#print(s.myAtoi("42"))
#print(s.myAtoi(" -42"))
print(s.myAtoi("1337c0d3"))
#print(s.myAtoi("0-1"))
#print(s.myAtoi("words and 987"))