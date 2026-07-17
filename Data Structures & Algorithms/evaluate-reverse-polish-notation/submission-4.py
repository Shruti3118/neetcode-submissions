class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","*","-","/"]
        for i in range(len(tokens)):
            if tokens[i] in operators:
                op1 = stack.pop()
                op2 = stack.pop()
                val = 0
                if tokens[i] == "+":
                    val = op2 + op1
                elif tokens[i] == "-":
                    val = op2 - op1
                elif tokens[i] == "*":
                    val = op2 * op1
                else:
                    val = int(float(op2) / op1) 
                stack.append(val)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]

                
        