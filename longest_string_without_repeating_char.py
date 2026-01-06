class Solution(object):
    def lengthOfLongestSubstring(self, s):
        current_str = []
        longest_str = []

        for ch in s:
            if ch in current_str:
                if len(current_str) > len(longest_str):
                    longest_str = current_str[:]
                idx = current_str.index(ch)
                current_str = current_str[idx + 1:]

            current_str.append(ch)

        if len(current_str) > len(longest_str):
                   longest_str = current_str[:]

        final_str = "".join(longest_str)
        return len(final_str), final_str



s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))     # (3, 'wke')
print(s.lengthOfLongestSubstring("abcabcbb"))   # (3, 'abc') یا یکی دیگر مثل 'bca'
print(s.lengthOfLongestSubstring("dvdf"))













