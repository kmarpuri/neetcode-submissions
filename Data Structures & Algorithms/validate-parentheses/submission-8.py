class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == ")" or c == "}" or c == "]":
                print(f"c is {c}")
                top = stack.pop()
                if ((top == '(' and c != ')') or (top == '{' and c != '}') or (top == '[' and c != ']')):
                    return False
        return len(stack) == 0
