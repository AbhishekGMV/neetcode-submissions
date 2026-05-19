class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {"}": "{", ")": "(", "]":"["}

        for c in s:
            if c in "([{":
                stack.append(c)
                continue
            if c in "})]":
                if stack and stack[-1] == braces[c]:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0