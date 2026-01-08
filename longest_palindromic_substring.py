class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        string_list = list(s)
        rev_string_list = string_list[::-1]
        palindrome_list = []

        size = len(string_list)

        for i in range(size):
            left = string_list[0:i + 1]
            right = rev_string_list[-(i + 1):]

            candidate = []
            best = []

            for j, k in zip(left, right):
                if j == k:
                    candidate.append(j)
                    if len(candidate) > len(best):
                        best = candidate[:]
                print("Candidate", candidate)

            if best == best[::-1]:
                palindrome_list.append(best)
            else:
                palindrome_list.append([])

        largest_list = max(palindrome_list, key=len, default=[])
        return "".join(largest_list)

s = Solution()
print(s.longestPalindrome("abb"))
