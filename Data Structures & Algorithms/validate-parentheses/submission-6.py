class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(', '}':'{', ']':'['}
        stack = []

        for paren in s:
            if paren in valid:
                if not stack or stack.pop() != valid[paren]: #no empty stack pop or if the stack does not pop a closing
                    return False
            else:
                stack.append(paren)

        return not stack #empty stack
