class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, longest, n = 0, 0, len(s)
        h_set = set()
        for right in range(len(s)):
            while s[right] in h_set:
                h_set.discard(s[left])
                left += 1
            curLength = (right - left) + 1
            if curLength > longest:
                longest = curLength
            h_set.add(s[right])
        return longest
