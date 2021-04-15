for tc in range(1, 11):
    N = int(input())
    infix = list(input())
    postfix = []
    stack = []
    operator = ["*", "/", "+", "-"]
    braket = ["(", ")"]


    def is_number(x):
        if x not in operator and x not in braket:
            return True
        else:
            return False

    def isp(token):  # isp : 스택의 top 연산자 우선순위
        if token == "*" or token == "/":
            return 2
        elif token == "+" or token == "-":
            return 1
        elif token == "(":
            return 0


    def icp(token):  # icp : 스택으로 들어갈 연산자의 우선순위
        if token == "(":
            return 3
        elif token == "*" or token == "/":
            return 2
        elif token == "+" or token == "-":
            return 1

    for i in infix:
        if is_number(i):
            postfix.append(i)
        elif i == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            if stack == []:
                stack.append(i)
            else:
                while isp(stack[-1]) >= icp(i):
                    postfix.append(stack.pop())
                    if stack == []:
                        break
                stack.append(i)
    while stack != []:
        postfix.append(stack.pop())

    tot = 0
    for i in postfix:
        if is_number(i):
            stack.append(i)
        elif i == '+':
            tot = int(stack.pop()) + int(stack.pop())
            stack.append(tot)
        else:
            tot = int(stack.pop()) * int(stack.pop())
            stack.append(tot)

    print(f'#{tc} {tot}')



