class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for s in strs:
            key = "".join(list(sorted(list(s))))
            if key not in words:
                words[key] = [s]
                continue
            words[key].append(s)
        return list(words.values())
            