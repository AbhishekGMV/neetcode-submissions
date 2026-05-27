class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-/*"

        for ch in tokens:
            if ch in ops:
                a = stack.pop()
                b = stack.pop()
                exp = str(b) + ch + str(a)
                stack.append(int(eval(exp)))
            else:
                stack.append(ch)
        return int(stack.pop())
