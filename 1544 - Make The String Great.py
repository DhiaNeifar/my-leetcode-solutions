class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and ((stack[-1].upper() == stack[-1] and char.lower() == char and stack[-1] == char.upper()) or
                           stack[-1].lower() == stack[-1] and char.upper() == char and stack[-1] == char.lower()):
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)