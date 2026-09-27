def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def infix_to_postfix(expression):
    stack = []
    result = ""

    for char in expression:
        if char.isalnum():
            result += char

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result += stack.pop()
            stack.append(char)

    while stack:
        result += stack.pop()

    return result


expr = "A+B*C"

print("Postfix:", infix_to_postfix(expr))