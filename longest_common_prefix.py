class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        def compare(list_of_strings, chars):
            for word in list_of_strings:
                if not word.startswith(chars):
                    return False
            return True

        first_word = strs[0]
        char_list = []

        for i in range(1, len(first_word) + 1):
            chars = first_word[:i]
            if compare(strs, chars):
                char_list.append(chars)
            else:
                break

        return max(char_list, key=len) if char_list else ""
s = Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))