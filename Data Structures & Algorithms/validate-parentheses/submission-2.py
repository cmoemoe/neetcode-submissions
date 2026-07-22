class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for symbol in s:
            if len(stack) == 0 and (symbol == "]" or symbol == "}" or symbol == ")"):
                return False

            if symbol == "[": 
                stack.append(symbol)
            if symbol == "(": 
                stack.append(symbol)
            if symbol == "{": 
                stack.append(symbol)
            
            if symbol == "]":
                if stack[-1] == "[":
                    stack.pop()
                else: 
                    return False
            if symbol == ")":
                if stack[-1] == "(":
                    stack.pop()
                else: 
                    return False
            if symbol == "}":
                if stack[-1] == "{":
                    stack.pop()
                else: 
                    return False

            print(stack)

        return len(stack) == 0
            

            