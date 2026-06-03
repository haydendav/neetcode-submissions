class Solution:
    def isValid(self, s: str) -> bool:
        closed = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s:
            if char in closed:
                if not stack or stack[-1] != closed[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return not stack
        