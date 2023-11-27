class Solution:
    def isValid(self, s):
    
        parentheses = {'(':')','[':']','{':'}'}
        stack = []   # Array Implementation of stack

        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                if not stack or parentheses[stack.pop()]!=c:
                #stack為空
                    return False
        return not stack