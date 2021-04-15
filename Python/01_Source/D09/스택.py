T = int(input())
for tc in range(1, T+1):
    A = input()
    top = -1
    for i in A:
        if i == '(':
            top += 1
        elif i == ')':
            top -= 1
        else:
            pass
        if top < 0:
            break