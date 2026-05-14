def prioritas(op):
    if op == '^':
        return 3
    elif op in "*/":
        return 2
    elif op in "+-":
        return 1
    else:
        return 0

def infix_ke_postfix(infix):
    stack = []
    postfix = ""

    for char in infix:
        # jika operand (A,B,C,...)
        if char.isalnum():
            postfix += char

        # jika buka kurung
        elif char == '(':
            stack.append(char)

        # jika tutup kurung
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # buang '('

        # jika operator
        else:
            while stack and prioritas(char) <= prioritas(stack[-1]):
                postfix += stack.pop()
            stack.append(char)

    # pop sisa operator
    while stack:
        postfix += stack.pop()

    return postfix


# Input user
infix = input("Masukkan ekspresi infix: ")
print("Postfix:", infix_ke_postfix(infix))