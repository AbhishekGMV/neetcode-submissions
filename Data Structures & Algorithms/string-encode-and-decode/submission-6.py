class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        while i < len(s):
            # read str length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1

            # read str and append
            word = s[j : j + length]
            decoded.append(word)

            # move i ptr to read next digit
            i = j + length

        return decoded
