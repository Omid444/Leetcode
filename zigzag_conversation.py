class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""]*numRows
        row = 0
        for char in s:
            rows[row] += char
            print(rows)

            if row == 0:
                angle = 1
            elif row == numRows - 1:
                angle = -1

            row += angle
            print(row)


        return "".join(rows)

s = Solution()
print(s.convert("PAYPALISHIRING",3))