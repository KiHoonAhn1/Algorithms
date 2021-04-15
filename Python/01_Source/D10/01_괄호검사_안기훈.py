T = int(input())
for tc in range(1, T+1):
    stack = []
    top = -1
    N = input()
    sentence = True

    for i in N:
        if i == '(':
            top += 1
            stack.append('(')
        elif i == '{':
            top += 1
            stack.append('{')

        if i == ')':
            if top >= 0 and stack[top] == '(':
                top -= 1
                stack.pop()
            else:
                sentence = False
        elif i == '}':
            if top >= 0 and stack[top] == '{':
                top -= 1
                stack.pop()
            else:
                sentence = False

    if stack == [] and sentence:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')