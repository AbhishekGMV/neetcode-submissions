class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        sizes = []

        for word in strs:
            sizes.append(len(word))

        for sz in sizes:
            encoded += str(sz) + ","
        encoded += "#"
        encoded += "".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        sizes = []

        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        i += 1
        res = []

        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz
        return res

