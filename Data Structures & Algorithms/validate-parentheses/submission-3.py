class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        validpairs = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in validpairs:
                if stack and stack[-1] == validpairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False

        # Time O(n)