class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        validstring = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in validstring:
                if stack and stack[-1] == validstring[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)

        return True if not stack else False

        #Time O(n)
        