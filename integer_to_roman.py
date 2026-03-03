class Solution:
    def is_first_digit_4_or_9(self, num):
        if str(num) == 4 or str(num) == 9:
            return True
        return False


    def intToRoman(self, num: int) -> str:
        symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
                 ]
        divisor = 1
        components = []
        while num >0:
            remainder = num % (divisor * 10)
            if remainder > 0:
                components.insert(0, remainder)

            num -= remainder
            divisor *= 10

        res = ""
        for val in components:

            for unit_val, unit_sym in symbols:
                while val >= unit_val:
                    res += unit_sym
                    val -= unit_val

        return res

            