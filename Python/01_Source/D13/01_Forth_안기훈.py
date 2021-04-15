T = int(input())
for tc in range(1, T+1):
    stack = []
    arr = list(input().split())
    for i in arr:
        try:
            if i == '.':
                if len(stack) == 1:
                    print(f'#{tc} {stack.pop()}')
                    break
                else:
                    print(f'#{tc} error')
                    break
            if i == '+' or i == '-' or i == '*' or i == '/':
                t1 = stack.pop()
                t2 = stack.pop() # 먼저 pop한게 t1 자리로 가야되는걸 생각 못하고 1시간 낭비함...
                if i == '+':
                    stack.append(t2+t1)
                elif i == '-':
                    stack.append(t2-t1)
                elif i == '*':
                    stack.append(t2*t1)
                elif i == '/':
                    stack.append(t2//t1)
            else:
                stack.append(int(i))
        except:
            print(f'#{tc} error')
            break