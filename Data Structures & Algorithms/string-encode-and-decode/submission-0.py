class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            for char in word:
                encoded += char
            encoded += "₹"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        curr = ""

        for char in s:
            if char == "₹":
                decoded.append(curr)
                curr = ""
                continue
            curr += char
        return decoded
