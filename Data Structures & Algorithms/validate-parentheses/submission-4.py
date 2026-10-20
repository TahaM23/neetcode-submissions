class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        validpairs = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in validpairs:     # closing bracket
                if stack and stack[-1] == validpairs[c]:
                    stack.pop()
                else:
                    return False
            else:                   # opening bracket
                stack.append(c)

        return not stack