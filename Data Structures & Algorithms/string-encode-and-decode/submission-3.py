class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            encoded_string += str(len(word)) + '#' + word
        print(encoded_string)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s) - 1:
            length = s[i]
            while s[i + 1].isdigit():
                length += s[i + 1]
                i += 1
            res.append(s[i + 2: i + 2 + int(length)])
            i = i + 2 + int(length)
        return res
