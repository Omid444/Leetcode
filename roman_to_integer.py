from itertools import count


class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "M": 1000, "CM": 900, "D": 500, "CD":400,
            "C": 100, "XC": 90, "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
        }

        position = 0
        s_list = list(s.strip())
        print(s_list)
        if s in symbols.keys():
            return symbols["s"]
        number = 0
        count = 0
        while count < len(s_list):
           if "".join(s_list[count:count+2]) in symbols:
               number += symbols["".join(s_list[count:count+2])]
               count += 2
           else:
               number += symbols[s_list[count]]
               count += 1
        return number


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))