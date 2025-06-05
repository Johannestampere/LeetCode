class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        hsh = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for p in s:
            if p in hsh:
                if stack and stack[-1] == hsh[p]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(p)
        
        if len(stack) == 0:
            return True
        else:
            return False