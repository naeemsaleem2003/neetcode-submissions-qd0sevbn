class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = []
        for char in tokens:
            if char == "+":
                result = int(output[-2]) + int(output[-1])
                output.pop()
                output.pop()
                output.append(result)
            elif char == "-":
                result = int(output[-2]) - int(output[-1])
                output.pop()
                output.pop()
                output.append(result)
            elif char == "*":
                result = int(output[-2]) * int(output[-1])
                output.pop()
                output.pop()
                output.append(result)
            elif char == "/":
                result = int(output[-2]) / int(output[-1])
                output.pop()
                output.pop()
                output.append(result)
            else:
                output.append(char)
        return int(output[-1])