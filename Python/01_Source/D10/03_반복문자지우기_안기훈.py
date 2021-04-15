T = int(input())
for tc in range(1, T+1):
    voca = input()
    stack = [' '] * 1000
    top = 0
    cnt = 0
    for a in voca:
        if stack[top] == a:
            stack[top] = ' '
            top -= 1
        else:
            top += 1
            stack[top] = a
    print(f'#{tc} {top}')