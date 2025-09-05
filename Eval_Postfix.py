def eval_postfix(expression: str) -> int:
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()  
            a = stack.pop()  
            
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    
    return stack[0]


print(eval_postfix("2 1 + 3 *"))   