class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in operator:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(
                        int(a / b),
                    )
            else:
                stack.append(int(token))
        return int(stack[0])