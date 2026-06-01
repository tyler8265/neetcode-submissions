class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        s = s.lower()
        l = list(s)
        for i in range(len(s)):
            if s[i].isalnum():
                res.insert(0, s[i])
        for i in range(len(l) - 1, -1, -1):
            if l[i].isalnum():
                continue
            l.remove(l[i])
        return res == l