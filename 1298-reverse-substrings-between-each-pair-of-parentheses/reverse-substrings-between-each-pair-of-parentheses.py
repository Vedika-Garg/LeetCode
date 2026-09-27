class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ")":
                stack.append(ch)
            else:
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())

                stack.pop()

                stack.extend(temp)
        
        return ("".join(stack))